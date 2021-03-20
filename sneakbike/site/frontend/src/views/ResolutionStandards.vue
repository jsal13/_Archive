<template>
  <div class="resolution-standards">
    <v-row justify="center">
      <v-col cols="2" />
      <v-col cols="8">
        <h1>Resolution Standards</h1>

        <div class="ml-6 mt-6">
          <h2>Sneakbike Standard Aspect Ratio</h2>
          <p>
            Due to the ease of setting a standard
            <b>aspect ratio</b> (AR) on a number of emulators, and because our overlays often have static sizes, we prefer to set all of our games, if possible, to the same AR.
          </p>

          <p>Specifically, we use 8:7 for every game we play.</p>

          <warning-card>
            In general, all Sneakbike games should be run in:
            <ul class="pt-2">
              <li>
                <b>8:7</b> ASPECT RATIO
              </li>
              <li>
                <b>544x476</b> OR SIMILAR
              </li>
            </ul>
          </warning-card>

          <v-btn depressed class="mb-4" @click="showReference = !showReference">Show/Hide Reference</v-btn>

          <div v-show="showReference">
            <h2>Standard Resolution Reference</h2>
            <warning-card>
              These resolutions are simply for reference and NOT to be used unless the above does not work for some reason. You should have a
              <i>very good reason</i> to deviate from the standard resolution above.
            </warning-card>

            <v-data-table
              dense
              hide-default-footer
              :headers="headers"
              :items="rows"
              class="elevation-1"
            />

            <warning-card>
              N64 games tend to have different resolutions, these should probably
              be looked at individually.
            </warning-card>
          </div>
        </div>
      </v-col>
      <v-col />
    </v-row>
  </div>
</template>

<script>
const headers = [
  {
    text: "Console",
    align: "start",
    sortable: false,
    value: "console",
  },
  {
    text: "Aspect Ratio",
    align: "center",
    sortable: false,
    value: "aspectRatio",
  },
  {
    text: "Example Resolution",
    align: "center",
    sortable: false,
    value: "exampleResolution",
  },
];

const rows = [
  { console: "NES", aspectRatio: "16:15", exampleResolution: "512x480" },
  { console: "SNES", aspectRatio: "8:7", exampleResolution: "544x476" },
  { console: "Genesis", aspectRatio: "10:7", exampleResolution: "640x448" },
  { console: "N64", aspectRatio: "17:12*", exampleResolution: "680x480*" },
];

export default {
  name: "ResolutionStandards",
  data() {
    return { headers, rows, showReference: false };
  },
};
</script>
