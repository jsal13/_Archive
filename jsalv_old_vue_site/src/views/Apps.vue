<template>
  <div class="home-apps">
    <v-container>
      <v-container>
        <v-row>
          <v-col class="col-10 offset-1">
            <h2 class="mb-5">Apps</h2>
            <v-row>
              <home-apps-card
                :image="require('@/assets/images/apps/sneakbike_readme_app.png')"
                :description="descriptionREADME"
                :title="'Sneakbike README App'"
                :link="'/app/readme-gen'"
                class="mx-4"
              />
              <home-apps-card
                :image="require('@/assets/images/apps/sneakbike_race_data_tool.png')"
                :description="descriptionSBRaceDataTool"
                :title="'Sneakbike Race Data Tool'"
                :link="'/app/race-data-tool'"
                class="mx-4"
              />
              <home-apps-card
                :image="require('@/assets/images/apps/sneakbike_gamepicker_game_tool.png')"
                :description="descriptionGamepickerGameInfo"
                :title="'Gamepicker Game Info Tool'"
                :link="'/app/gamepicker-game-info'"
                class="mx-4"
              />
              <home-apps-card
                :image="require('@/assets/images/apps/new_jersey.jpg')"
                :description="descriptionLicensePlatePractice"
                :title="'License Plate Practice App'"
                :link="'/app/license-plate-practice'"
                class="mx-4"
              />
              <home-apps-card
                :image="require('@/assets/images/apps/topic-generator.png')"
                :description="descriptionTopicGenerator"
                :title="'Topic Generator'"
                :link="'/app/topic-generator'"
                class="mx-4"
              />
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
  </div>
</template>

<script>
import HomeAppsCard from '@/components/HomeAppsCard.vue';

const descriptionREADME = `An app which allows the user to input controls, objectives, and hints for SNES, NES, Genesis, etc., games.
We use this for Sneakbike, the retro mystery-game racing charity.`;

const descriptionSBRaceDataTool = 'A tool we use in Sneakbike to simplify updating a few different fields with the same data.';

const descriptionLicensePlatePractice = 'A tool to help learn blurred license plate identification for use in, for example, GeoGuessr.';

const descriptionGamepickerGameInfo = 'Used to help gamepickers give info to commentators for Sneakbike.';

const descriptionTopicGenerator = 'Used to help generate topics with random nouns, verbs, adjectives; eg, for writing or naming.';

export default {
  name: 'Apps',
  components: { HomeAppsCard },
  data() {
    return {
      descriptionREADME,
      descriptionSBRaceDataTool,
      descriptionLicensePlatePractice,
      descriptionGamepickerGameInfo,
      descriptionTopicGenerator,
    };
  },
};
</script>
