<template>
  <v-container>
    <v-row>
      <v-col>
        <v-expansion-panels inset>
          <v-expansion-panel
            v-for="vehicle in vehicles"
            :key="vehicle.id"
          >
            <v-expansion-panel-header>
              <div>
                <div class="mb-1">
                  <v-icon v-if="vehicle.status === 'available'" color="green">mdi-check-circle</v-icon>
                  <v-icon v-else-if="vehicle.status === 'charging'" color="blue">mdi-ev-station</v-icon>
                  <v-icon v-else color="red">mdi-close-circle</v-icon>
                  {{ vehicle.licensePlate }}
                  <span class="font-weight-light font-italic">
                    {{ vehicle.model }}
                  </span>
                </div>
                <v-progress-linear value="12" color="cyan" rounded :buffer-value="vehicle.status === 'charging' ? 12 : 0" :stream="vehicle.status === 'charging'" ></v-progress-linear>
              </div>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  created() {
    this.$http.get('/api/vehicle/').then(resp => {
      this.vehicles.push(...resp.data.data)
    })
  },
  data() {
    return {
      vehicles: []
    }
  }
}
</script>

<style>

</style>