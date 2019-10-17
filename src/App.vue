<template>
  <v-app>
    <sidebar :drawer="drawer" v-if="isLoggedIn"></sidebar>

    <v-app-bar
      app
      dark
      clipped-left
      color="primary"
      v-if="isLoggedIn">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="headline text-uppercase">
        <span>eGO</span>
        <span class="font-weight-light">N</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu
      >
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-account-circle</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item :to="{ name: 'profile' }">
            <v-list-item-title>Profile</v-list-item-title>
          </v-list-item>
          <v-list-item @click="logout">
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
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
import Sidebar from '@/components/Sidebar'

export default {
  name: 'App',
  components: {
    Sidebar
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  data() {
    return {
      drawer: false
    };
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
      this.$router.push({ name: 'login' })
    }
  }
};
</script>
