<template>
  <div
    class="bingo-card"
    v-bind:style="{
      'background-color': isActive ? cardBGColor : cardDefaultBGColor,
      'border-color': cardBorderColor,
      color: cardTextColor
    }"
    @click="isActive = !isActive"
  >
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "BingoCard",
  props: { cardBGColor: { type: String } },
  data() {
    return { isActive: false };
  },
  computed: {
    cardDefaultBGColor() {
      return this.$vuetify.theme.dark ? "#121212" : "#fefefe";
    },
    cardBorderColor() {
      return this.$vuetify.theme.dark ? "#333333" : "#121212";
    },
    cardTextColor() {
      return this.$vuetify.theme.dark ? "#bbbbbb" : "#121212";
    },
  },
};
</script>

<style scoped>
.bingo-card {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  border: 2px solid;
  font-size: 1em;
  font-family: "Roboto", sans-serif;
  padding: 0.5em;
}
</style>
