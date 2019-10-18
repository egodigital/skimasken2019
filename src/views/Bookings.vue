<template>
  <v-container>
    <v-form  @submit.prevent="submitForm" ref="form" lazy-validation>
      <v-row>
        <v-col cols="12" md="4">
          <datetime-picker
            :timePickerProps="{'allowed-minutes': [0, 15, 30, 45]}"
            label="From"
            v-model="form.start_time"
            :rules="rules.datetimeRules"
            required
          ></datetime-picker>
        </v-col>
        <v-col cols="12" md="4">
          <datetime-picker
            :timePickerProps="{'allowed-minutes': [0, 15, 30, 45]}"
            label="To"
            v-model="form.end_time"
            :rules="rules.datetimeRules"
            required
          ></datetime-picker>
        </v-col>
        <v-col cols="12" md="4">
          <v-select
            :items="vehicles"
            label="Vehicle"
            v-model="form.vehicle_id"
            :rules="rules.vehicleRules"
            required
          ></v-select>
        </v-col>
        <v-col cols="12">
          <v-text-field
            label="Destination"
            v-model="form.destination"
            :rules="rules.destinationRules"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-subheader class="pl-0">Distance (in km)</v-subheader>
          <v-text-field type="number" v-model="form.distance"></v-text-field>
          <v-slider
            v-model="form.distance"
            thumb-label
            min="5"
            max="850"
            required
          ></v-slider>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="4">
          <v-checkbox
            v-model="form.fuzzy"
            label="Fuzzy?"
            hint="Take a booking anywhere inbetween the given datetime range as soon as the selected vehicle is available."
            persistent-hint
          ></v-checkbox>
        </v-col>
        <v-col cols="4">
          <v-checkbox
            v-model="form.public"
            label="Public?"
            hint="Place the booking onto the blackboard to make it publicy available to others nearby."
            persistent-hint
          ></v-checkbox>
        </v-col>
        <v-col cols="4" align-self="center" class="text-center">
          <v-btn type="submit" color="blue accent-2" class="white--text">
            <v-icon>mdi-plus</v-icon>Add booking
          </v-btn>
        </v-col>
      </v-row>
      <hr />
      <v-row>
        <v-col>
          <v-data-table
            :headers="headers"
            :items="bookings"
            hide-default-footer
            class="elevation-1"
          >
            <template v-slot:item.vehicle="{ value }">
              {{ value.licensePlate }} ({{ value.model }})
            </template>
            <template v-slot:item.start_time="{ value }">
              {{ moment(value) }}
            </template>
            <template v-slot:item.end_time="{ value }">
              {{ moment(value) }}
            </template>
          </v-data-table>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
import DatetimePicker from "@/components/DatetimePicker";
import moment from 'moment-timezone'

export default {
  components: {
    DatetimePicker
  },
  async created() {
    // Fetch all vehicles
    const responseVehicles = await this.$http.get("/api/vehicle/")
    for (const vehicle of responseVehicles.data.data) {
      this.vehicles.push({
        text: `${vehicle.licensePlate} (${vehicle.model})`,
        value: vehicle.id
      });
    }
    
    // Fetch my bookings
    const responseBookings = await this.$http.get('/api/booking/me')
    const bookings = responseBookings.data
    for(const booking of bookings) {
      booking.vehicle = responseVehicles.data.data.filter(v => v.id === booking.vehicle_id)[0]
    }

    this.bookings.push(...bookings)
  },
  data() {
    return {
      form: {
        start_time: "",
        end_time: "",
        fuzzy: false,
        public: false,
        distance: 0,
        destination: "",
        vehicle_id: 0
      },
      rules: {
        datetimeRules: [v => !!v || "Please select a datetime."],
        vehicleRules: [v => !!v || "Please select a vehicle."],
        destinationRules: [v => !!v || "Please select a destination."]
      },
      vehicles: [],
      headers: [
        { text: "Booking ID", value: "id" },
        { text: "Vehicle", value: "vehicle" },
        { text: "From", value: "start_time" },
        { text: "To", value: "end_time" },
      ],
      bookings: []
    };
  },
  methods: {
    moment(date) {
      return moment(date).format('MM/DD/YYYY HH:mm')
    },
    submitForm() {
      if(this.$refs.form.validate() === false)
        return
      
      this.$http.post(`/api/vehicle/${this.form.vehicle_id}/bookings`, this.form)
      .then(resp => {
        const booking = resp.data

        this.$http.get(`/api/vehicle/${booking.vehicle_id}`).then(resp => {
          booking.vehicle = resp.data.data
          this.bookings.push(booking)
        })

        this.$refs.form.reset()
        this.form.fuzzy = false
        this.form.public = false
      })
    }
  }
};
</script>

<style>
</style>