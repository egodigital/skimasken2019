from datetime import timedelta, datetime
import bisect 

SLOT_WIDTH = timedelta(seconds=60*15)

class Booking:
    def __init__(self, start, end, predicted_km):
        self.start = start
        self.end = end
        self.predicted_km = predicted_km

    def slot_count(self):
        return (self.end - self.start) / SLOT_WIDTH

    def __repr__(self):
        return f"{self.start}: {self.slot_count()} slots"

    def __lt__(self, other):
        return self.start < other.start

    def overlaps(self, other):
        if self.start <= other.start and self.end > other.start:
            print("overlap right")
            return True
        if other.start <= self.start and other.end > self.start:
            print("overlap left")
            return True

        return False


class BookingOptimizer:
    def __init__(self, charging_function, timedelta_max):
        self.timedelta_max = timedelta_max
        self.charging_function = charging_function
        self.bookings = list()
    
    def book(self, booking):
        if booking.start > (datetime.utcnow() + self.timedelta_max) or booking.start < datetime.utcnow():
            print("invalid dates")
            return False
        index = bisect.bisect_left(self.bookings, booking)
        print(index)
        if index > 0 and booking.overlaps(self.bookings[index - 1]):
            return False
        if index < len(self.bookings) and booking.overlaps(self.bookings[index]):
            return False
        self.bookings.insert(index, booking)
        print(booking, self.bookings)
        return True


def simple_charge(current_charge):
    return min(150.0, current_charge + 20) # km at max charge: 150km, charging 20km per slot

opt = BookingOptimizer(simple_charge, timedelta(seconds=60*60*24*30))

opt.book(Booking(datetime(year=2019, month=10, day=18, hour=12, minute=0), 
                datetime(year=2019, month=10, day=18, hour=13, minute=0), 100))
opt.book(Booking(datetime(year=2019, month=10, day=18, hour=12, minute=0), 
                datetime(year=2019, month=10, day=18, hour=13, minute=0), 100))