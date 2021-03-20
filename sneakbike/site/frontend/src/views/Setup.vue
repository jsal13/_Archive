<template>
  <div class="runner-setup">
    <v-container>
      <v-row>
        <v-col cols="10" offset="1">
          <v-tabs v-model="tab" centered icons-and-text>
            <v-tabs-slider></v-tabs-slider>

            <v-tab href="#runners">
              Runners
              <v-icon>mdi-controller-classic</v-icon>
            </v-tab>

            <v-tab href="#producers">
              Producers
              <v-icon>mdi-radio-tower</v-icon>
            </v-tab>
          </v-tabs>
        </v-col>
      </v-row>

      <v-row justify="center" class="pt-4">
        <v-col cols="10" offset="1">
          <v-tabs-items :value="tab">
            <v-tab-item :value="'runners'">
              <SetupRunnerText />
            </v-tab-item>
            <v-tab-item :value="'producers'">
              <SetupProducerText />
            </v-tab-item>
          </v-tabs-items>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import SetupProducerText from "@/components/Setup/ProducerText.vue";
import SetupRunnerText from "@/components/Setup/RunnerText.vue";

export default {
  name: "Setup",
  computed: {
    tab: {
      set(tab) {
        this.$router.replace({ query: { ...this.$route.query, tab } });
      },
      get() {
        return this.$route.query.tab;
      },
    },
  },
  components: { SetupProducerText, SetupRunnerText },
};
</script>

