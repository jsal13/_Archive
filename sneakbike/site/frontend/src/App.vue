<template>
  <v-app>
    <v-app-bar app hide-on-scroll class="primary">
      <v-col cols="6">
        <v-flex class="d-flex">
          <v-menu offset-y open-on-hover>
            <template v-slot:activator="{ on, attrs }">
              <v-btn text>
                <v-icon large v-bind="attrs" v-on="on">mdi-menu</v-icon>
              </v-btn>
            </template>
            <v-list dense class="pa-0">
              <template>
                <div v-for="(k, v, idx) in pages" :key="`dropdown-menu-${v}-${idx}`">
                  <v-list-item class="secondary">
                    <v-list-item-title class="text-overline">{{v}}</v-list-item-title>
                  </v-list-item>
                  <v-divider class="menu-divider" />
                  <v-list-item
                    class="menu-list-item"
                    v-for="(item, jdx) in k"
                    :key="`dropdown-menu-item-${idx}-${jdx}`"
                    :to="item.route"
                  >
                    <v-list-item-subtitle>{{item.name}}</v-list-item-subtitle>
                  </v-list-item>
                </div>
              </template>
            </v-list>
          </v-menu>

          <v-toolbar-title id="site-title">
            <router-link class="text--primary" to="/">Sneakbike</router-link>
          </v-toolbar-title>
        </v-flex>
      </v-col>
      <v-col>
        <v-flex class="d-flex">
          <v-spacer />
          <v-switch
            class="pt-3"
            color="grey lighten-4"
            v-model="$vuetify.theme.dark"
            inset
            flat
            hide-details
            :prepend-icon="$vuetify.theme.dark ? 'mdi-weather-night' : 'mdi-white-balance-sunny'"
          ></v-switch>

          <v-divider vertical inset />
          <div
            class="title-bar-icon"
            v-for="item in titleBarIcons"
            :key="`title-bar-icon-${item.name}`"
          >
            <v-btn icon :href="item.link" target="_blank">
              <v-icon large>{{ item.icon }}</v-icon>
            </v-btn>
          </div>
        </v-flex>
      </v-col>
    </v-app-bar>

    <v-main>
      <v-container mt-10>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "App",
  data() {
    return {
      drawer: false,
    };
  },
  computed: {
    ...mapState("homepage", ["titleBarIcons", "pages"]),
  },
};
</script>