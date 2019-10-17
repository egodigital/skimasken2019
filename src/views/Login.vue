<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-card-text>
            <v-form
              @submit.prevent="login"
              id="form-login"
              lazy-validation
              ref="form">
              <v-text-field
                v-model="username"
                label="Login"
                name="login"
                prepend-icon="mdi-account"
                type="text"
                :rules="rules.usernameRules"
                required
              ></v-text-field>

              <v-text-field
                v-model="password"
                id="password"
                label="Password"
                name="password"
                prepend-icon="mdi-lock"
                type="password"
                :rules="rules.passwordRules"
                required
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn type="submit" form="form-login" color="primary">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      rules: {
        usernameRules: [v => !!v || "Username is required"],
        passwordRules: [v => !!v || "Password is required"]
      }
    }
  },
  methods: {
    login() {
      if(this.$refs.form.validate() === false)
        return
      
      this.$store
        .dispatch("login", { username: this.username, password: this.password })
    }
  }
};
</script>

<style>
</style>