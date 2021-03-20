<template>
  <div class="hkr-item-table">
    <div style="margin-top: 1.0rem;">
      <div v-for="(data, loc, idx) in arrayLocDataObj" :key="`rect-${loc}-${idx}`">
        <HKRItemRect
          v-if="arrayLocDataObj[loc]['show']"
          @hideRow="toggleLocationInLocDataObj({'loc': loc})"
          :loc="loc"
          :zindex="idx + 10"
          class="hkr-item-rectangle"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import HKRItemRect from "@/components/HollowKnight/HKRItemRect.vue";

export default {
  name: "HKRItemTable",
  components: { HKRItemRect },
  computed: {
    ...mapState("hkr", ["arrayLocDataObj"]),
  },
  methods: {
    ...mapMutations("hkr", ["toggleLocationInLocDataObj"]),
  },
};
</script>

<style scoped>
.hkr-item-rectangle {
  margin-top: -6px;
}
</style>