<template>
  <v-expansion-panel>
    <v-expansion-panel-header>Areas</v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-flex class="d-flex flex-wrap">
        <div v-for="(data, loc, idx) in arrayLocDataObj" :key="`chip-${loc}-${idx}`">
          <v-chip
            class="ma-1"
            :class="{'dimmed-chip': !arrayLocDataObj[loc]['show']}"
            :color="arrayLocDataObj[loc]['background']"
            @click="toggleLocationInLocDataObj({'loc': loc})"
          >
            <span class="chip-text">{{ arrayLocDataObj[loc]['displayName'] }}</span>
          </v-chip>
        </div>
      </v-flex>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  name: "HKRPills",
  // components: { HKRItemRect },
  computed: {
    ...mapState("hkr", ["arrayLocDataObj"]),
  },
  methods: {
    ...mapMutations("hkr", ["toggleLocationInLocDataObj"]),
  },
};
</script>

<style scoped>
.chip-text {
  color: white;
  -webkit-user-select: none; /* Safari */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* IE10+/Edge */
  user-select: none; /* Standard */
  cursor: default;
}

.dimmed-chip {
  opacity: 0.5;
}
</style>