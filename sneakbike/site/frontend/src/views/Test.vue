<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="8" offset="2" class="d-flex">
          <v-select v-model="jen" :items="items" label="Jen" outlined dense></v-select>
          <v-select v-model="mel" :items="items" label="Melat0nin" outlined dense></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8" offset="2" class="d-flex">
          <v-select v-model="ace" :items="items" label="Ace" outlined dense></v-select>
          <v-select v-model="kingcake" :items="items" max label="KingCake" outlined dense></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8" offset="2" class="d-flex">
          <v-select v-model="ghost" :items="items" label="Ghost" outlined dense></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8" offset="2">
          <v-btn>Submit</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
const items = [
  "Do spikey floor bois",
  "Colors or whatever",
  "more lifeblood",
  "two wingwangs",
];

export default {
  name: "Test",
  data() {
    return {
      items,
      jen: null,
      mel: null,
      ace: null,
      kingcake: null,
      ghost: null,
    };
  },
};
</script>