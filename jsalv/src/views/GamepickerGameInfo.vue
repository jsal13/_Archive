<template>
  <div class="gamepicker-game-info">
    <v-row justify="center">
      <v-col cols="10" offset="1">
        <h1>Gamepicker Game Info Tool</h1>

        <p class="mb-4">Used to help gamepickers give info to commentators for Sneakbike.</p>

        <hr />

        <h2 class="mb-4">Game 1</h2>
        <v-text-field
          v-model="g1Title"
          class="px-2"
          label="Game 1 Title"
          placeholder="Game 1 Title"
          outlined
        />
        <v-text-field
          v-model="g1Console"
          class="px-2"
          label="Game 1 Console"
          placeholder="Game 1 Console"
          outlined
        />
        <v-text-field
          v-model="g1Objective"
          class="px-2"
          label="Game 1 Potential Objective"
          placeholder="Game 1 Potential Objective"
          outlined
        />
        <a
          :href="`https://www.google.com/search?q=${g1Title.replace(' ', '+')}+${g1Console}+manual`"
          target="_blank"
        >{{ `https://www.google.com/search?q=${g1Title.replace(' ', '+')}+${g1Console}+manual` }}</a>
        <v-text-field
          v-model="g1Manual"
          class="px-2"
          label="Game 1 Manual"
          placeholder="Game 1 Manual"
          outlined
        />
        <a
          :href="`https://www.google.com/search?q=${g1Title.replace(' ', '+')}+wikipedia`"
          target="_blank"
        >{{ `https://www.google.com/search?q=${g1Title.replace(' ', '+')}+wikipedia` }}</a>
        <v-text-field
          v-model="g1Wiki"
          class="px-2"
          label="Game 1 Wikipedia"
          placeholder="Game 1 Wikipedia"
          outlined
        />
        <a
          :href="`https://www.google.com/search?q=${g1Title.replace(' ', '+')}+youtube`"
          target="_blank"
        >{{ `https://www.google.com/search?q=${g1Title.replace(' ', '+')}+youtube` }}</a>
        <v-text-field
          v-model="g1Playthrough"
          class="px-2"
          label="Game 1 Playthrough Video"
          placeholder="Game 1 Playthrough Video"
          outlined
        />
        <v-textarea
          v-model="g1Notes"
          class="px-2"
          label="Game 1 Notes"
          placeholder="Game 1 Notes"
          outlined
        />

        <hr />

        <h2 class="mb-4">Game 2</h2>
        <v-text-field
          v-model="g2Title"
          class="px-2"
          label="Game 2 Title"
          placeholder="Game 2 Title"
          outlined
        />
        <v-text-field
          v-model="g2Console"
          class="px-2"
          label="Game 2 Console"
          placeholder="Game 2 Console"
          outlined
        />
        <v-text-field
          v-model="g2Objective"
          class="px-2"
          label="Game 2 Potential Objective"
          placeholder="Game 2 Potential Objective"
          outlined
        />
        <a
          :href="`https://www.google.com/search?q=${g2Title.replace(' ', '+')}+${g2Console}+manual`"
          target="_blank"
        >{{ `https://www.google.com/search?q=${g2Title.replace(' ', '+')}+${g2Console}+manual` }}</a>
        <v-text-field
          v-model="g2Manual"
          class="px-2"
          label="Game 2 Manual"
          placeholder="Game 2 Manual"
          outlined
        />
        <a
          :href="`https://www.google.com/search?q=${g2Title.replace(' ', '+')}+wikipedia`"
          target="_blank"
        >{{ `https://www.google.com/search?q=${g2Title.replace(' ', '+')}+wikipedia` }}</a>
        <v-text-field
          v-model="g2Wiki"
          class="px-2"
          label="Game 2 Wikipedia"
          placeholder="Game 2 Wikipedia"
          outlined
        />
        <a
          :href="`https://www.google.com/search?q=${g2Title.replace(' ', '+')}+youtube`"
          target="_blank"
        >{{ `https://www.google.com/search?q=${g2Title.replace(' ', '+')}+youtube` }}</a>
        <v-text-field
          v-model="g2Playthrough"
          class="px-2"
          label="Game 2 Playthrough Video"
          placeholder="Game 2 Playthrough Video"
          outlined
        />
        <v-textarea
          v-model="g2Notes"
          class="px-2"
          label="Game 2 Notes"
          placeholder="Game 2 Notes"
          outlined
        />

        <v-btn @click="downloadHTML">Submit</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { saveAs } from 'file-saver';

export default {
  name: 'GamepickerGameInfo',
  data() {
    return {
      g1Title: '',
      g1Objective: '',
      g1Console: '',
      g1Manual: '',
      g1Wiki: '',
      g1Playthrough: '',
      g1Notes: '',
      g2Title: '',
      g2Objective: '',
      g2Console: '',
      g2Manual: '',
      g2Wiki: '',
      g2Playthrough: '',
      g2Notes: '',
    };
  },
  methods: {
    downloadHTML() {
      const file = new File([this.createHTML()], 'README_Gameplayer_Game_Info.html', {
        type: 'text/plain;charset=utf-8',
      });
      saveAs(file);
    },

    createHTML() {
      return `
    <html><body>

    <h1>Game 1: (${this.g1Console}) ${this.g1Title}</h1>
    <h2>Objective: ${this.g1Objective}</h2>
    <ul>
    <li>Manual: <a href="${this.g1Manual}" target="_blank">${this.g1Manual}</a></li>
    <li>Wiki: <a href="${this.g1Wiki}" target="_blank">${this.g1Wiki}</a></li>
    <li>Manual: <a href="${this.g1Playthrough}" target="_blank">${this.g1Playthrough}</a></li>
    <li>Playthrough: <a href="${this.g1Manual}" target="_blank">${this.g1Manual}</a></li>
    <li>Notes: ${this.g1Notes}</li>
    </ul>

    <h1>Game 2: (${this.g2Console}) ${this.g2Title}</h1>
    <h2>Objective: ${this.g2Objective}</h2>
    <ul>
    <li>Manual: <a href="${this.g2Manual}" target="_blank">${this.g2Manual}</a></li>
    <li>Wiki: <a href="${this.g2Wiki}" target="_blank">${this.g2Wiki}</a></li>
    <li>Manual: <a href="${this.g2Playthrough}" target="_blank">${this.g2Playthrough}</a></li>
    <li>Playthrough: <a href="${this.g2Manual}" target="_blank">${this.g2Manual}</a></li>
    <li>Notes: ${this.g2Notes}</li>
    </ul>

    </body></html>
    `;
    },
  },
};
</script>

<style scoped>
</style>
