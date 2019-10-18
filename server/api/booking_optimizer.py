import requests
import random
import logging
from http import HTTPStatus
from datetime import datetime, timedelta, tzinfo
from flask import request, current_app
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import reqparse
import flask_login
import bisect

from server.models.booking import BookingModel, booking_schema, bookings_schema, booking_parser
from server.extensions.database import db

log = logging.getLogger(__name__)
api = Namespace('booking_optimizer', description='Optimizer calculates optimal bookings.')

@api.route('/<string:vehicle_id>')
class BookingOptimizer_Lars(Resource):
    
    max_booking_delta = timedelta(seconds=60*60*24*60)
    load_speed_per_hour = 80 # km
    max_load = 150 # km just a guess, ist vehicle-spezifisch
    km_lower_threshold = 20
    
    @flask_login.login_required
    @api.doc(responses={
        HTTPStatus.OK: 'Success',
        HTTPStatus.UNAUTHORIZED: 'Not authorized'
    })
    @api.expect(booking_parser)
    def get(self, vehicle_id):
        bookings = BookingModel.query.filter(BookingModel.vehicle_id == vehicle_id, BookingModel.end_time > datetime.utcnow()).all()
        
        args = booking_parser.parse_args()
        args.update({"environment_id": "", "id": "dummy", "email": "", "vehicle_id": vehicle_id})
        booking = booking_schema.load(args, session=db.session)
        db.session.add(booking) # workaround teil 1wegen tzinfo datetime vergleiche
        db.session.commit()

        log.debug(f"Requested booking: {booking}")
        suggested_bookings = list()

        # sanity check
        if booking.start_time > (datetime.utcnow() + self.max_booking_delta) or booking.start_time < datetime.utcnow():
            return "invalid dates", HTTPStatus.CONFLICT

        bookings.sort()
        log.debug(bookings)


        data = requests.get(current_app.config["API_BASE"] + f"/vehicles/{vehicle_id}/signals", headers={"X-Api-Key": current_app.config["API_KEY"]}).json()
        calculated_remaining_distance = data["data"]["calculated_remaining_distance"]
        log.debug(f"calc_est_km: {calculated_remaining_distance}")

        index = bisect.bisect_left(bookings, booking)
        if self.fits(booking, bookings, index, calculated_remaining_distance):
            suggested_bookings.append(booking)
        else:
            log.debug("didnt fit")


        # workaround teil 2
        dummy_booking = BookingModel.query.filter(BookingModel.id == "dummy").first()
        if dummy_booking:
            db.session.delete(dummy_booking)
            db.session.commit()

        def dump(bok):
            return {
                "booking": booking_schema.dump(bok),
                "shift": (booking.start_time - bok.start_time).total_seconds() // 60,
                "estimated_km_at_booking_end": bok.estimated_km if hasattr(bok, "estimated_km") else -1
            }

        return {
            "current_calculated_remaining_distance": calculated_remaining_distance,
            "suggested_bookings": [dump(bok) for bok in suggested_bookings],
            "existing_bookings": [dump(bok) for bok in bookings],
        }, HTTPStatus.OK

    def fits(self, booking, bookings, index, start_km):
        log.debug(f"test fit: {index}")
        if index > 0 and booking.overlaps(bookings[index - 1]):
            log.debug("overlap left")
            return False
        if index < len(bookings) and booking.overlaps(bookings[index]):
            log.debug("overlap right")
            return False

        curr_km = start_km
        curr_time = datetime.utcnow()
        log.debug(f"start at: {start_km}km at {curr_time}")
        if len(bookings) > 0:
            diff_minutes = (bookings[0].start_time - curr_time).total_seconds() // 60
            log.debug(f"diff minutes: {diff_minutes}")
            if diff_minutes < 0:
                km_per_minute = bookings[0].get_duration() / bookings[0].distance
                curr_km = min(self.max_load, curr_km + abs(diff_minutes) * km_per_minute)
                curr_time = bookings[0].start_time
                log.debug(f"corrected: start at: {start_km}km at {curr_time}")

        # calculate estimated km at the index
        for i in range(index):
            curr_km = self.simple_battery_loading_function(curr_time, bookings[i].start_time, curr_km)
            curr_km = max(0, curr_km - bookings[i].distance)
            log.debug(f"usage to {curr_km}")

            bookings[i].estimated_km = curr_km
            curr_time = bookings[i].end_time
            log.debug(f"at {curr_time}")

        curr_km = self.simple_battery_loading_function(curr_time, booking.start_time, curr_km)
        curr_km = max(0, curr_km -  booking.distance)
        log.debug(f"requested booking usage at {curr_km}")

        booking.estimated_km = curr_km
        curr_time = booking.end_time
        log.debug(f"at {curr_time}")

        if booking.estimated_km < self.km_lower_threshold:
            log.debug("minmal km threshold reached")
            return False
        
        log.debug("check if booking does not ruin later bookings")
        for i in range(index, len(bookings)):
            curr_km = self.simple_battery_loading_function(curr_time, bookings[i].start_time, curr_km)
            if curr_km == self.max_load:
                log.debug("safe point reached in following bookings")
                return True
            curr_km = max(0, curr_km - bookings[i].distance)
            log.debug(f"usage to {curr_km}")

            bookings[i].estimated_km = curr_km
            curr_time = bookings[i].end_time
            log.debug(f"at {curr_time}")

            if bookings[i].estimated_km < self.km_lower_threshold:
                log.debug("minmal km threshold reached for a following booking")
                return False
        return True

    def simple_battery_loading_function(self, start_time, end_time, curr_remaining_km):
        # approx. die "nachgeladenen" Km innerhalb zweier Zeitpunkte
        # zusätzlich mögliche faktoren, die die Ladegeschwindigkeit beeinflussen lönnten:
        # - non-lineares Laden, abhängig vom aktuellen Ladestand
        # - Tages/Jahreszeitabhängiges Ladeverhalten (wegen verscheidenen Temperaturen)

        approx_load = (end_time - start_time).total_seconds() * (self.load_speed_per_hour / 3600)
        res = min(self.max_load, curr_remaining_km + approx_load)
        log.debug(f"load to {res}, approx load {approx_load}")
        return res
