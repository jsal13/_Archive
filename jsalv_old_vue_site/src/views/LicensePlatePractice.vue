<template>
  <div class="license-plate-practice">
    <v-card class="mx-auto container" max-width="350">
      <v-card-text>
        <v-row align="center" class="mb-5">
          <v-col cols="6">
            <v-img
              :src="currentLicensePlatePath"
              :style="styleRandomBlur"
              contain
              :height="randomLicensePicHeight"
            />
          </v-col>
          <v-col cols="6">
            <v-btn @click="CheckState">Submit</v-btn>
            <v-btn class="mt-2" @click="NextState">Next State</v-btn>
          </v-col>
        </v-row>
        <v-row class="mb-5">
          <v-autocomplete v-model="userGuess" :items="states" dense />
        </v-row>
        <v-row>
          <span class="state-name" v-html="msgCheckState" />
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
/* eslint-disable */
const stateToStateAbbr = {
  alabama: 'AL',
  alaska: 'AK',
  arizona: 'AZ',
  arkansas: 'AR',
  california: 'CA',
  colorado: 'CO',
  connecticut: 'CT',
  delaware: 'DE',
  florida: 'FL',
  georgia: 'GA',
  hawaii: 'HI',
  idaho: 'ID',
  illinois: 'IL',
  indiana: 'IN',
  iowa: 'IA',
  kansas: 'KS',
  kentucky: 'KY',
  louisiana: 'LA',
  maine: 'ME',
  maryland: 'MD',
  massachusetts: 'MA',
  michigan: 'MI',
  minnesota: 'MN',
  mississippi: 'MS',
  missouri: 'MO',
  montana: 'MT',
  nebraska: 'NE',
  nevada: 'NV',
  new_hampshire: 'NH',
  new_jersey: 'NJ',
  new_mexico: 'NM',
  new_york: 'NY',
  north_carolina: 'NC',
  north_dakota: 'ND',
  ohio: 'OH',
  oklahoma: 'OK',
  oregon: 'OR',
  pennsylvania: 'PA',
  rhode_island: 'RI',
  south_carolina: 'SC',
  south_dakota: 'SD',
  tennessee: 'TN',
  texas: 'TX',
  utah: 'UT',
  vermont: 'VT',
  virginia: 'VA',
  washington: 'WA',
  west_virginia: 'WV',
  wisconsin: 'WI',
  wyoming: 'WY',
};
/* eslint-enable */

export default {
  name: 'LicensePlatePractice',
  data() {
    return {
      stateToStateAbbr,
      states: Object.values(stateToStateAbbr),
      styleRandomBlur: '',
      randomLicensePicHeight: 100,
      msgCheckState: '',
      currentLicensePlatePath: '',
      currentState: '',
      currentStateAbbr: '',
      userGuess: '',
    };
  },

  created() {
    this.GetImage();
  },
  methods: {
    GetRandomBlur() {
      this.styleRandomBlur = `-webkit-filter: blur(${Math.floor(Math.random() * 5 + 2)}px);`;
    },

    GetRandomLicensePicHeight() {
      this.randomLicensePicHeight = Math.floor(Math.random() * 55 + 20);
    },

    GetImage() {
      this.GetRandomBlur();
      this.GetRandomLicensePicHeight();

      const n = Math.floor(Math.random() * Object.keys(this.stateToStateAbbr).length);
      this.currentState = Object.keys(this.stateToStateAbbr)[n];
      this.currentStateAbbr = this.stateToStateAbbr[this.currentState];
      this.currentLicensePlatePath = `/license_plates/${this.currentState}.jpg`;
    },

    CheckState() {
      if (this.userGuess === this.currentStateAbbr) {
        this.msgCheckState = '<span style="color: green;"> Correct!</span>';
      } else {
        this.msgCheckState = `<span style="color: red;">${this.currentState.replace('_', ' ')}</span>`;
      }
      this.styleRandomBlur = '';
    },
    NextState() {
      this.GetImage();
      this.userGuess = '';
      this.msgCheckState = '';
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
}

.state-name {
  font-weight: bold;
  text-transform: capitalize;
}
</style>
