<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="3">
        <datetime-picker :timePickerProps="{'allowed-minutes': [0, 15, 30, 45]}" label="From" v-model="date.from"></datetime-picker>
      </v-col>
      <v-col cols="12" md="3">
        <datetime-picker :timePickerProps="{'allowed-minutes': [0, 15, 30, 45]}" label="To" v-model="date.to"></datetime-picker>
      </v-col>
      <v-col cols="12" md="2">
        <v-select
          :items="vehicles"
          label="Standard"
        ></v-select>
      </v-col>
      <v-col cols="12" md="1">
        <v-checkbox
          v-model="isFuzzy"
          label="Fuzzy?"
        ></v-checkbox>
      </v-col>
      <v-col cols="12" md="3" v-if="isFuzzy">
        <v-text-field
          label="Duration in minutes"
          type="number"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-data-table
          :headers="headers"
          :items="bookings"
          hide-default-footer
          class="elevation-1"
        >
          <template v-slot:item.user="{ value }">
            <v-avatar size="35">
              <v-img src="https://cdn.vuetifyjs.com/images/john.jpg"></v-img>
            </v-avatar>
            {{ value.user_name }}
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DatetimePicker from '@/components/DatetimePicker'

export default {
  components: {
    DatetimePicker
  },
  created() {
    this.$http.get('/api/vehicle/').then(resp => {
      for(const vehicle of resp.data.data) {
        this.vehicles.push({
          text: `${vehicle.licensePlate} (${vehicle.model})`,
          value: vehicle.id
        })
      }
    })
  },
  data() {
    return {
      date: {
        from: '',
        to: ''
      },
      fuzzyDate: {
        from: '',
        to: ''
      },
      isFuzzy: false,
      vehicles: [],
      headers: [
        { text: 'User', value: 'user' },
        { text: 'Booking ID', value: 'id' },
        { text: 'Vehicle', value: 'vehicle' },
        { text: 'Status', value: 'vehicle' },
      ],
      bookings: [
        { id: '2322adeqw', vehicle: 'AC-EGO 123 (Life 20)', user: { user_name: 'John Doe' }},
        { id: '9t8bwhfww', vehicle: 'AC-EGO 124 (Life 30)', user: { user_name: 'John Doe' }},
        { id: '34efbtz6u', vehicle: 'AC-EGO 125 (Life 40)', user: { user_name: 'John Doe' }},
        { id: '242fdcwf2', vehicle: 'AC-EGO 126 (Life 50)', user: { user_name: 'John Doe' }},
        { id: 'fdsgww43f', vehicle: 'AC-EGO 127 (Life 60)', user: { user_name: 'John Doe' }}
      ]
    }
  }
}
</script>

<style>

</style>