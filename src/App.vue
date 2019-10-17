<template>
  <v-app>
    <v-app-bar
      app
      dark
      color="primary">
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
export default {
  name: 'App',
  components: {
  },
  data: () => ({
    //
  }),
};
</script>
