<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="text-center">
        <v-avatar size="150">
          <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
        </v-avatar>
        <p class="display-3">John Doe</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3" sm="2" offset-sm="1" align-self="center">
        <v-avatar size="80">
          <img src="../assets/icons/level_icons/car_sharer.svg" alt="John"/>
        </v-avatar>
      </v-col>
      <v-col cols="9" sm="8" align-self="center">
        <v-progress-linear color="pink" value="67" height="30" rounded>Level 1</v-progress-linear>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3" sm="2" offset-sm="1" align-self="center">
        <v-avatar size="80">
          <img src="../assets/icons/level_icons/charger.svg" alt="John" />
        </v-avatar>
      </v-col>
      <v-col cols="9" sm="8" align-self="center">
        <v-progress-linear color="light-blue" value="46" height="30" rounded>Level 4</v-progress-linear>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3" sm="2" offset-sm="1" align-self="center">
        <v-avatar size="80">
          <img src="../assets/icons/level_icons/eco_driver.svg" alt="John" />
        </v-avatar>
      </v-col>
      <v-col cols="9" sm="8" align-self="center">
        <v-progress-linear color="light-green" value="15" height="30" rounded>Level 8</v-progress-linear>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3" sm="2" offset-sm="1" align-self="center">
        <v-avatar size="80">
          <img src="../assets/icons/level_icons/reliability.svg" alt="John" />
        </v-avatar>
      </v-col>
      <v-col cols="9" sm="8" align-self="center">
        <v-progress-linear color="orange" value="89" height="30" rounded>Level 2</v-progress-linear>
      </v-col>
    </v-row>
    <br>
    <v-row>
      <v-col cols="12">
        <h1 class="display-3 text-center">
          <v-icon x-large>mdi-trophy</v-icon>
          Achievements
        </h1>
        <v-list>
          <v-list-item
            v-for="achievement in achievements"
            :key="achievement.achievement_id"
            three-line>
            <v-list-item-avatar tile>
              <v-img src="../assets/achievements/Alman.svg"></v-img>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>
                {{ achievement.title }}
                <span class="font-weight-bold" v-if="$store.state.auth.user.level < achievement.level_req">
                  <v-tooltip top>
                    <template v-slot:activator="{ on }">
                      <v-icon v-on="on">mdi-alert-decagram</v-icon>
                    </template>
                    <span>
                      Level {{ achievement.level_req }} required
                    </span>
                  </v-tooltip>
                </span>
              </v-list-item-title>
              <v-list-item-subtitle v-text="achievement.description"></v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-icon>
              <v-badge
                overlap
                :color="typeColors[achievement.level_type] || 'blue-grey'">
                <template v-slot:badge>{{ achievement.score }}</template>
                <v-icon>mdi-coins</v-icon>
              </v-badge>
            </v-list-item-icon>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      typeColors: {
        CHARGER: 'light-blue',
        CAR_SHARER: 'pink',
        ECO_DRIVER: 'light-green',
        RELIABILITY: 'orange'
      },
      achievements: [
        {
          achievement_id: 1,
          type: 'SIMPLE',
          level_req: 0,
          level_type: null,
          score: 20,
          title: 'First Journey',
          description: 'Take your first journey and get started to make the world a better place.',
          thumbnail: null
        },
        {
          achievement_id: 2,
          type: 'LEVEL',
          level_req: 3,
          level_type: 'CHARGER',
          score: 10,
          title: 'First Journey',
          description: 'Take your first journey and get started to make the world a better place.',
          thumbnail: null
        },
        {
          achievement_id: 3,
          type: 'LEVEL',
          level_req: 5,
          level_type: 'ECO_DRIVER',
          score: 35,
          title: '10 Journeys',
          description: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam',
          thumbnail: null
        }
      ]
    }
  }
};
</script>

<style>
</style>