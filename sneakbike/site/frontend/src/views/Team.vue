<template>
  <div class="team">
    <v-row justify="center" align="center">
      <h1 class="team">Sneakbike Admin</h1>
    </v-row>

    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <v-row :align="'center'" :justify="'center'">
          <v-col
            v-for="(item, index) in admin"
            :key="`portrait-${index}`"
            style="flex-grow: 0 !important"
          >
            <TeamPortrait
              :name="item.name"
              :imgSrc="item.imgSrc"
              :hoverInfo="item.jobs"
              :twitchUsername="item.twitchUsername"
              :descriptionText="item.descriptionText"
            />
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <br />
    <br />

    <v-row justify="center" align="center">
      <h1 class="team">Sneak-ops Team</h1>
    </v-row>

    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <v-row :align="'center'" :justify="'center'">
          <v-col
            v-for="(item, index) in team"
            :key="`portrait-${index}`"
            style="flex-grow: 0 !important"
          >
            <TeamPortrait
              :name="item.name"
              :imgSrc="item.imgSrc"
              :hoverInfo="item.jobs"
              :twitchUsername="item.twitchUsername"
              :descriptionText="item.descriptionText"
            />
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState } from "vuex";
import TeamPortrait from "@/components/TeamPortrait.vue";

export default {
  name: "Team",
  computed: {
    ...mapState("team", ["team", "admin"]),
  },
  components: { TeamPortrait },
};
</script>
