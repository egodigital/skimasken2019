<template>
  <v-container>
    <blackboard-card v-for="booking of bookings" :key="booking.id" :booking="booking"></blackboard-card>
  </v-container>
</template>

<script>
import BlackboardCard from '@/components/BlackboardCard'

export default {
  components: {
    BlackboardCard
  },
  created() {
    this.$http.get('/api/booking/').then(resp => (this.bookings = resp.data))
  },
  data() {
    return {
      bookings: []
    }
  }
};
</script>

<style>
</style>