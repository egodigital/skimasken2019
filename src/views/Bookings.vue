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
      vehicles: []
    }
  }
}
</script>

<style>

</style>