<template>
  <div class="readme-game-box">
    <v-card width="400">
      <v-card-title>Game {{cardNum + 1}} ({{consoles[cardNum]}})</v-card-title>
      <v-card-subtitle>
        <v-flex class="d-flex">
          <v-chip
            class="ma-1"
            :class="{'dimmed': consoles[cardNum] !== 'SNES'}"
            @click="setControllerType({console: 'SNES', cardNum: cardNum})"
          >SNES</v-chip>
          <v-chip
            class="ma-1"
            :class="{'dimmed': consoles[cardNum] !== 'NES'}"
            @click="setControllerType({console: 'NES', cardNum: cardNum})"
          >NES</v-chip>
          <v-chip
            class="ma-1"
            :class="{'dimmed': consoles[cardNum] !== 'Genesis'}"
            @click="setControllerType({console: 'Genesis', cardNum: cardNum})"
          >Genesis</v-chip>
        </v-flex>

        <v-flex class="d-flex"></v-flex>
      </v-card-subtitle>
      <v-card-text>
        <v-text-field
          :label="'Objective'.toUpperCase()"
          @input="e => setObjective({val: e, cardNum: cardNum})"
        />
        <v-text-field
          :label="'Hint'.toUpperCase()"
          @input="e => setHint({val: e, cardNum: cardNum})"
        />
        <div
          v-for="(button, idx) in Object.keys(controllerData[cardNum])"
          :key="`button-input-${cardNum}-${idx}-${button}`"
        >
          <v-text-field
            :label="button.toUpperCase()"
            @input="e => setControllerButton({val: e, cardNum: cardNum, button: button})"
          />
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  name: "ReadmeGameBox",
  props: { cardNum: Number },
  computed: {
    ...mapState("readmeGenerator", ["controllerData", "consoles"]),
  },
  methods: {
    ...mapMutations("readmeGenerator", [
      "setControllerType",
      "setControllerButton",
      "setHint",
      "setObjective",
    ]),
  },
  created() {
    this.setControllerType({ cardNum: this.cardNum, console: "SNES" });
    this.setHint({ cardNum: this.cardNum, val: "" });
    this.setObjective({ cardNum: this.cardNum, val: "" });
  },
};
</script>

<style>
.dimmed {
  opacity: 0.4;
}
</style>