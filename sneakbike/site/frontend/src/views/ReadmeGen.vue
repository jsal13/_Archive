<template>
  <div class="game-readme-gen">
    <v-main>
      <v-col cols="2">
        <v-select :items="[1, 2, 3, 4]" label="Number of Games" v-model="numGames" />
        <v-btn @click="generateHTML">Generate</v-btn>
      </v-col>
      <v-row>
        <div v-for="n in numGamesArray" :key="`card-col-${n}`">
          <ReadmeGameBox :cardNum="n" />
        </div>
      </v-row>
    </v-main>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { saveAs } from "file-saver";
import ReadmeGameBox from "@/components/ReadmeGameBox.vue";
import generateReadmeHTML from "@/utils/readmeRender.js";

export default {
  name: "ReadmeGen",
  data() {
    return { numGames: 2, readmeHTML: "" };
  },
  computed: {
    ...mapState("readmeGenerator", ["controllerData", "hints", "objectives"]),
    numGamesArray() {
      return [...Array(this.numGames).keys()];
    },
  },
  components: { ReadmeGameBox },
  methods: {
    generateHTML() {
      this.readmeHTML = generateReadmeHTML(
        this.numGames,
        this.controllerData,
        this.objectives,
        this.hints
      );
      this.downloadHTML();
    },
    downloadHTML() {
      let file = new File([this.readmeHTML], "README_Sneakbike.html", {
        type: "text/plain;charset=utf-8",
      });
      saveAs(file);
    },
  },
};
</script>
