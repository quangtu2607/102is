<template>
  <nav>

    <v-snackbar v-model="snackbar" :timeout="4000" top color="success">
      <span>New project added.</span>
      <v-btn text color="white" @click="snackbar = false">Close</v-btn>
    </v-snackbar>

    <v-app-bar flat class="grey lighten-4">
      <button @click="$router.push('/')">
        <img src="~@/assets/logo.png" height="150" width="250" margin-top="100">
      </button>
      <!-- <v-app-bar-nav-icon @click="drawer = !drawer" class="grey--text"></v-app-bar-nav-icon> -->
      <!-- <v-toolbar-title class="text-uppercase grey--text"> -->
        <!-- <span class="font-weight-light">Server</span> -->
        <!-- <span class="font-weight-bold">Dashboard</span>
      </v-toolbar-title>
      <v-spacer /> -->
      <!-- <span class="font-weight-bold">Dashboard</span> -->

      <!-- Dropdown menu -->
      <!-- <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text depressed slot="activator" v-on="on" v-bind="attrs" class="grey--text">
            <v-icon left>expand_more</v-icon>
            <span>Menu</span>
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu> -->

      <!--<v-btn text color="grey">
        <span>Sign out</span>
        <v-icon right>exit_to_app</v-icon>
      </v-btn>-->
    </v-app-bar>

    <!-- <v-navigation-drawer app v-model="drawer" class="grey lighten-4">

      <v-list>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-item-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer> -->
    

  </nav>
</template>

<script>

export default {
  name: "Navbar",
  data() {
    return {
      drawer: false,
      links: [
        { icon: 'sports_soccer', text: 'Match Overview', route: '/'},
        // { icon: 'settings', text: 'Processes', route: '/processes' },
        { icon: 'paid', text: 'FaBet88', route: '/users' },
      ],
      snackbar: false
    }
  }
}
</script>

<style scoped>
/deep/ .v-toolbar__content {
  padding-top: 50px !important;
  padding-left: 0px;
}

</style>