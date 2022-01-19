<template>
  <v-app id="sandbox">
    <SideNavContent
      :mini-variant="primaryDrawer.mini"
      :model="primaryDrawer.model"
    />

    <v-app-bar app>
      <v-app-bar-nav-icon
        @click.stop="primaryDrawer.model = !primaryDrawer.model"
      />
      <v-toolbar-title>Vuetify</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <v-row
          align="center"
          justify="center"
        >
          <v-col cols="10">
            <div id="app">
              <router-view></router-view>
              <h1>{{ apiAddress }}</h1>
              <p>hi</p>
            </div>
          </v-col>

          <v-col cols="10">
            <v-card>
              <v-card-text>
                <v-row>
                  <v-col
                    cols="12"
                    md="6"
                  >
                    <span>Scheme</span>
                    <v-switch
                      v-model="$vuetify.theme.dark"
                      primary
                      label="Dark"
                    />
                  </v-col>
                  <v-col
                    cols="12"
                    md="6"
                  >
                    <v-switch
                      v-model="primaryDrawer.mini"
                      label="Mini"
                      primary
                    />
                  </v-col>
                </v-row>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn text>Cancel</v-btn>
                <v-btn
                  text
                  color="primary"
                >Submit</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer
      :inset="true"
      app
    >
      <span class="px-4">Dog Tinder &copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import axios from "axios";
import SideNavContent from './components/SideNavContent';

export default {
  name: "app",
  data() {
    return {
      drawers: ['Default (no property)', 'Permanent', 'Temporary'],
      primaryDrawer: {
        model: null,
        type: 'default (no property)',
        clipped: false,
        floating: false,
        mini: false,
      },
    };
  },
  components: {
    SideNavContent
  },
  mounted() {
    axios({
      method: "get",
      url: `${this.apiAddress}/dog`,
      params: { dog_type: "American_Husky" }
    }).then(response => {
      console.log(response.data); /* eslint-disable-line */
    });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
