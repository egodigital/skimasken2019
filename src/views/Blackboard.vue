<template>
  <v-container>
    <blackboard-card :booking="{}"></blackboard-card>
    <blackboard-card :booking="{}"></blackboard-card>
  </v-container>
</template>

<script>
import BlackboardCard from '@/components/BlackboardCard'

export default {
  components: {
    BlackboardCard
  }
};
</script>

<style>
</style>