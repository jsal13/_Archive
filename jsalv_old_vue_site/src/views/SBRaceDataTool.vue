<template>
  <div class="race-data-tool">
    <v-row justify="center">
      <v-col cols="10" offset="1">
        <h1>Race Data Tool</h1>

        <p class="mb-4">
          Used to populate Nightbot commands and the
          <a
            :href="sneaksquadURL"
            target="_blank"
          >Sneaksquad Googledoc</a>.
        </p>

        <hr />
        <div class="my-4">
          <v-flex class="d-flex flex-wrap">
            <v-text-field
              v-model="nameC1"
              class="px-2"
              label="Commentator 1"
              placeholder="Commentator 1"
              outlined
            />
            <v-text-field
              v-model="nameC2"
              class="px-2"
              label="Commentator 2"
              placeholder="Commentator 2"
              outlined
            />
            <v-text-field
              v-model="nameP1"
              class="px-2"
              label="Producer 1"
              placeholder="Producer 1"
              outlined
            />
            <v-text-field
              v-model="nameP2"
              class="px-2"
              label="Producer 2"
              placeholder="Producer 2"
              outlined
            />
            <v-text-field
              v-model="nameRunner1"
              class="px-2"
              label="Runner 1"
              placeholder="Runner 1"
              outlined
            />
            <v-text-field
              v-model="nameRunner2"
              class="px-2"
              label="Runner 2"
              placeholder="Runner 2"
              outlined
            />
            <v-text-field
              v-model="nameRunner3"
              class="px-2"
              label="Runner 3"
              placeholder="Runner 3"
              outlined
            />
            <v-text-field
              v-model="nameRunner4"
              class="px-2"
              label="Runner 4"
              placeholder="Runner 4"
              outlined
            />
            <v-text-field
              v-model="nameGamePicker"
              class="px-2"
              label="Game Picker"
              placeholder="Game Picker"
              outlined
            />
            <v-select
              v-model="difficulty"
              :items="difficultyList"
              class="px-2"
              label="Race Diffulty Level"
              outlined
            />
          </v-flex>
          <v-text-field
            v-model="gamesAndConsole"
            class="px-2"
            label="Games and System"
            placeholder="(SNES) Ace Ventura 2, Zombies ate The Mask"
            outlined
          />
        </div>
        <hr />

        <div class="my-4">
          <h3 class="mb-4">Nightbot Commands:</h3>

          <ul>
            <li class="command-item mb-2 accent--text">!game Retro</li>
            <li
              class="command-item mb-2 accent--text"
            >!title Sneakbike Mystery Race with Friends! :']</li>
            <li class="command-item mb-2 accent--text">!commands edit !runners {{ runnersString }}</li>
            <li
              class="command-item mb-2 accent--text"
            >!commands edit !commentators The lovely voices you're hearing: {{ commentatorsString }}</li>
          </ul>
        </div>
        <hr />

        <div class="my-4">
          <h3 class="mb-4">Wiki Records Code:</h3>
          <p>
            Copy-paste this code into the source code of
            <a
              href="https://wiki.sneak.bike/e/en/general-resources/sneakbike-races"
              target="_blank"
            >the wiki for Sneakbike race history</a>. Go to the page and hit "Edit" to look at the source code.
          </p>
          <prism language="html">{{ wikiCode }}</prism>
        </div>

        <div class="my-4">
          <h3 class="mb-4">Sneaksquad Row:</h3>
          <p>
            Copy-paste the row values into the
            <a
              :href="sneaksquadURL"
              target="_blank"
            >Sneaksquad Googledoc</a> starting at the "Level" column. You'll have to manually input the date and VOD.
          </p>
          <table>
            <tr>
              <th>Level</th>
              <th>Commentators</th>
              <th>P1</th>
              <th>P2</th>
              <th>Game Picker</th>
              <th>Runners</th>
              <th>Games</th>
            </tr>
            <tr>
              <td>{{ difficulty !== null ? difficulty.toLowerCase() : "" }}</td>
              <td>{{ [nameC1, nameC2].filter(x => x).map(x => x.toLowerCase()).join(", ") }}</td>
              <td>{{ nameP1 ? nameP1.toLowerCase() : nameP1 }}</td>
              <td>{{ nameP2 ? nameP2.toLowerCase() : nameP2 }}</td>
              <td>{{ nameGamePicker ? nameGamePicker.toLowerCase() : nameGamePicker }}</td>
              <td>{{ [nameRunner1, nameRunner2, nameRunner3, nameRunner4].filter(x => x).map(x => x.toLowerCase()).join(", ") }}</td>
              <td>{{ gamesAndConsole }}</td>
            </tr>
          </table>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Prism from 'vue-prism-component';

const sneaksquadURL = 'https://docs.google.com/spreadsheets/d/1HjUhWhGxIt8CMUG3uLbplxpnZq0h3ikcVPGRTUaa-ws/edit?usp=sharing';

export default {
  name: 'RaceDataTool',
  components: { Prism },
  data() {
    return {
      nameC1: null,
      nameC2: null,
      nameP1: null,
      nameP2: null,
      nameGamePicker: null,
      nameRunner1: null,
      nameRunner2: null,
      nameRunner3: null,
      nameRunner4: null,
      gamesAndConsole: null,
      difficulty: 'Beginner',
      difficultyList: ['Beginner', 'Intermediate'],
      sneaksquadURL,
    };
  },
  computed: {
    runnersString() {
      return this.addTwitchURL([this.nameRunner1, this.nameRunner2, this.nameRunner3, this.nameRunner4]).join(' || ');
    },
    commentatorsString() {
      return this.addTwitchURL([this.nameC1, this.nameC2]).join(' || ');
    },
    wikiCode() {
      return `<tr>
  <td>MM/DD/YYYY</td>
  <td>${this.difficulty !== null ? this.difficulty.toLowerCase() : ''}</td>
  <td>${[this.nameC1, this.nameC2]
    .filter((x) => x)
    .map((x) => x.toLowerCase())
    .join(', ')}</td>
  <td>${this.nameGamePicker ? this.nameGamePicker.toLowerCase() : this.nameGamePicker}</td>
  <td>${[this.nameRunner1, this.nameRunner2, this.nameRunner3, this.nameRunner4]
    .filter((x) => x)
    .map((x) => x.toLowerCase())
    .join(', ')}</td>
  <td>${this.gamesAndConsole}</td>
  <td><a href="LINKTOYOUTUBE" target="_blank">Link</a></td>
</tr>`;
    },
  },
  methods: {
    addTwitchURL(sArray) {
      return sArray.map((s) => (s !== null ? `https://twitch.tv/${s}` : null)).filter((x) => x);
    },
  },
};
</script>

<style scoped>
ul {
  padding: 0;
}

.command-item {
  list-style: none;
  font-size: 1.2rem;
}

table {
  width: 100%;
}

table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
  font-size: 0.75rem;
}
th {
  background-color: #999999;
}

td {
  max-width: 150px;
  word-wrap: break-word;
}

.theme--dark.v-application code {
  background-color: #ffffff00;
}
</style>
