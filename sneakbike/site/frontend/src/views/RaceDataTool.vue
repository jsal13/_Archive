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
              class="px-2"
              label="C1"
              placeholder="Commentator 1"
              v-model="nameC1"
              outlined
            />
            <v-text-field
              class="px-2"
              label="C2"
              placeholder="Commentator 2"
              v-model="nameC2"
              outlined
            />
            <v-text-field
              class="px-2"
              label="P1"
              placeholder="Producer 1"
              v-model="nameP1"
              outlined
            />
            <v-text-field
              class="px-2"
              label="P2"
              placeholder="Producer 2"
              v-model="nameP2"
              outlined
            />
            <v-text-field
              class="px-2"
              label="Runner1"
              placeholder="Runner 1"
              v-model="nameRunner1"
              outlined
            />
            <v-text-field
              class="px-2"
              label="Runner2"
              placeholder="Runner 2"
              v-model="nameRunner2"
              outlined
            />
            <v-text-field
              class="px-2"
              label="Runner3"
              placeholder="Runner 3"
              v-model="nameRunner3"
              outlined
            />
            <v-text-field
              class="px-2"
              label="Runner4"
              placeholder="Runner 4"
              v-model="nameRunner4"
              outlined
            />
            <v-text-field
              class="px-2"
              label="GP1"
              placeholder="Game Picker"
              v-model="nameGamePicker"
              outlined
            />
            <v-text-field
              class="px-2"
              label="Race Diffulty Level"
              placeholder="Beginner"
              v-model="difficulty"
              outlined
            />
          </v-flex>
          <v-text-field
            class="px-2"
            label="Games and System"
            placeholder="(SNES) Ace Ventura 2, Zombies ate The Mask"
            v-model="gamesAndConsole"
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
            <li class="command-item mb-2 accent--text">!commands edit !runners {{runnersString}}</li>
            <li
              class="command-item mb-2 accent--text"
            >!commands edit !commentators The lovely voices you're hearing: {{commentatorsString}}</li>
          </ul>
        </div>
        <hr />

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
              <td>{{ difficulty !== null ? difficulty.toLowerCase() : ""}}</td>
              <td>{{ [nameC1, nameC2].filter(x => x).join(", ") }}</td>
              <td>{{ nameP1 }}</td>
              <td>{{ nameP2 }}</td>
              <td>{{ nameGamePicker }}</td>
              <td>{{ [nameRunner1, nameRunner2, nameRunner3, nameRunner4].filter(x => x).join(", ")}}</td>
              <td>{{ gamesAndConsole }}</td>
            </tr>
          </table>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
const sneaksquadURL =
  "https://docs.google.com/spreadsheets/d/1HjUhWhGxIt8CMUG3uLbplxpnZq0h3ikcVPGRTUaa-ws/edit?usp=sharing";

export default {
  name: "RaceDataTool",
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
      difficulty: null,
      sneaksquadURL,
    };
  },
  computed: {
    runnersString() {
      return this.addTwitchURL([
        this.nameRunner1,
        this.nameRunner2,
        this.nameRunner3,
        this.nameRunner4,
      ]).join(" || ");
    },
    commentatorsString() {
      return this.addTwitchURL([this.nameC1, this.nameC2]).join(" || ");
    },
  },
  methods: {
    addTwitchURL(sArray) {
      return sArray
        .map((s) => {
          return s !== null ? `https://twitch.tv/${s}` : null;
        })
        .filter((x) => x);
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
</style>
