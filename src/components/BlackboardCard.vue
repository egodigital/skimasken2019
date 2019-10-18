<template>
  <v-card max-width="344" class="d-inline-block ma-2" shaped>
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="https://cdn.vuetifyjs.com/images/john.jpg"></v-img>
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="headline">John Doe</v-list-item-title>
        <v-list-item-subtitle>AC-EGO 123 (Life 40)</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <hr>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>Today 4:00pm</v-list-item-title>
        <v-list-item-subtitle>Begin</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>8:00pm</v-list-item-title>
        <v-list-item-subtitle>End</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-card-actions>
      <v-btn>
        Request
        <v-icon class="light-green--text">mdi-hand-right</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    booking: {
      type: Object,
      required: true
    }
  }
};
</script>

<style>
</style>