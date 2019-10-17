<template>
  <v-app>
    <v-app-bar
      app
      dark
      color="primary"
      v-if="isLoggedIn">
      <v-toolbar-title class="headline text-uppercase">
        <span>eGO</span>
        <span class="font-weight-light">N</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>

    <v-footer>
    </v-footer>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  data: () => ({
    //
  }),
};
</script>
