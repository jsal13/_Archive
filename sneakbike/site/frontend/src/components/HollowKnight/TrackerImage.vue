<template>
  <div class="tracker-image">
    <img
      :src="require(`@/assets/hollow_knight/${item}.png`)"
      :class="{ 'item-found': itemFound }"
      @click="toggleItemFound()"
      :width="width"
      :height="height"
      :alt="`${item}`"
      :title="`${item}`"
    />
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  name: "TrackerImage",
  props: {
    item: String,
    name: String,
    width: Number,
    height: Number,
  },
  computed: {
    ...mapState("hkr", ["itemFoundState"]),
    itemFound() {
      return this.itemFoundState[this.name];
    },
  },
  methods: {
    ...mapMutations("hkr", ["setItemFoundState"]),
    toggleItemFound() {
      this.setItemFoundState({
        name: this.name,
        value: !this.itemFoundState[this.name],
      });
      this.$emit("itemToggled");
    },
  },
  created() {
    this.setItemFoundState({ name: this.name, value: false });
  },
};
</script>

<style>
.item-found {
  opacity: 0.3;
}
img {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
  padding-left: 1px !important;
  padding-right: 1px !important;
}
</style>