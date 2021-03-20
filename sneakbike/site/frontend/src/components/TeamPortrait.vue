<template>
  <div class="team-portrait">
    <v-tooltip bottom color="#00000000">
      <template v-slot:activator="{ on, attrs }">
        <a :href="`https://twitch.tv/${twitchUsername}`" target="_blank">
          <v-img
            :src="require(`@/assets/team_pictures/${imgSrc}`)"
            aspect-ratio="1"
            height="125"
            width="125"
            class="grey lighten-2"
            alt="Portrait"
            v-bind="attrs"
            v-on="on"
            @mouseover="hover = true"
            @mouseleave="hover = false"
          >
            <v-expand-transition>
              <div
                v-if="hover"
                class="d-flex transition-fast-in-fast-out blue darken-2 font-weight-medium v-card--reveal subtitle-1 white--text"
                style="height: 100%;"
              >{{ name }}</div>
            </v-expand-transition>
          </v-img>
        </a>
      </template>
      <v-card>
        <v-card-subtitle class="pb-0" v-html="hoverInfo" />
        <v-card-text class="text--primary">{{ descriptionText }}</v-card-text>
      </v-card>
    </v-tooltip>
  </div>
</template>

<script>
export default {
  name: "TeamPortrait",
  props: {
    name: String,
    hoverInfo: String,
    imgSrc: String,
    twitchUsername: String,
    descriptionText: String,
  },
  data() {
    return {
      hover: false,
    };
  },
};
</script>

<style lang="scss" scoped>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.5;
  position: absolute;
  width: 100%;
}
</style>
