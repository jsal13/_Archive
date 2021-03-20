<template>
  <v-expansion-panel>
    <v-expansion-panel-header>Options</v-expansion-panel-header>
    <v-expansion-panel-content>
      <div v-if="allowBlueMode">
        <p
          class="text-subtitle-2"
        >Blue Mode: If you want to use this on OBS as a tracker, Window Capture the browser, turn on Blue Background Mode below, and set an OBS Chroma Key Filter with custom color rgb(0, 0, 255).</p>
        <v-switch
          :label="'OBS Blue Background Mode?'"
          @change="toggleBlueScreen"
          v-model="blueScreen"
        />
      </div>
      <v-switch
        :label="'Show Dreamers?'"
        @change="toggleDreamersAndRefresh()"
        :input-value="showDreamers"
      />
      <v-switch
        :label="'Show Abilities?'"
        @change="toggleAbilitiesAndRefresh()"
        :input-value="showAbilities"
      />
      <v-switch
        :label="'Show Useful Items?'"
        @change="toggleUsefulItemsAndRefresh()"
        :input-value="showUsefulItems"
      />

      <div v-if="allowSetTimer">
        <v-switch
          :class="{'mb-6': showTimer}"
          :label="'Display items after X minutes?'"
          @change="v => toggleSliderAndSetTimerValue(v, {val: v ? 120 : 0})"
        />
        <v-slider
          v-if="showTimer"
          @change="v => setTimerValue({val: v})"
          :value="timerValue"
          tick-size="4"
          min="0"
          max="240"
          step="30"
          thumb-label="always"
        ></v-slider>
      </div>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import { mapState, mapMutations, mapActions } from "vuex";

export default {
  name: "HKRItemToggle",
  data() {
    return { blueScreen: false, showTimer: false };
  },
  props: {
    allowSetTimer: { type: Boolean, default: true },
    allowBlueMode: { type: Boolean, default: true },
  },
  computed: {
    ...mapState("hkr", [
      "showDreamers",
      "showAbilities",
      "showUsefulItems",
      "timerValue",
    ]),
  },
  methods: {
    ...mapMutations("hkr", ["setTimerValue"]),
    ...mapActions("hkr", [
      "toggleDreamersAndRefresh",
      "toggleAbilitiesAndRefresh",
      "toggleUsefulItemsAndRefresh",
    ]),
    toggleBlueScreen() {
      document.getElementById("app").style.background = this.blueScreen
        ? "rgb(0,0,255)"
        : "";
    },
    toggleSliderAndSetTimerValue(v, payload) {
      this.showTimer = v;
      this.setTimerValue(payload);
    },
  },
  beforeDestroy() {
    document.getElementById("app").style.background = "";
  },
};
</script>