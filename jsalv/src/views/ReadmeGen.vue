<template>
  <div class="readme-gen">
    <v-container>
      <v-main>
        <v-col cols="2" class="mb-4">
          <v-select v-model="numGames" :items="[1, 2, 3, 4]" label="Number of Games" />
          <v-btn @click="generateHTML">Generate</v-btn>
        </v-col>
        <v-row>
          <div v-for="n in numGamesArray" :key="`card-col-${n}`">
            <readme-game-box :card-num="n" />
          </div>
        </v-row>
      </v-main>
    </v-container>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import { saveAs } from 'file-saver';
import ReadmeGameBox from '@/components/apps/readme-gen/ReadmeGameBox.vue';
import generateReadmeHTML from '@/components/apps/readme-gen/readmeRender';

export default {
  name: 'ReadmeGen',
  components: { ReadmeGameBox },
  data() {
    return { numGames: 2, readmeHTML: '' };
  },
  computed: {
    ...mapState('readmeGenerator', ['controllerData', 'hints', 'objectives']),
    numGamesArray() {
      return [...Array(this.numGames).keys()];
    },
  },
  methods: {
    generateHTML() {
      this.readmeHTML = generateReadmeHTML(this.numGames, this.controllerData, this.objectives, this.hints);
      this.downloadHTML();
    },
    downloadHTML() {
      const file = new File([this.readmeHTML], 'README_Sneakbike.html', {
        type: 'text/plain;charset=utf-8',
      });
      saveAs(file);
    },
  },
};
</script>
