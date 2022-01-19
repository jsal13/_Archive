<template>
  <div class="home-skills-progress-section mr-4">
    <h2 class="mb-4">{{ title }}</h2>
    <p v-for="(row, idx) in skills" :key="`skill-${idx}`">
      <span :style="{color: skillColors[row.itemType]}">{{ row.item }}</span>
    </p>
  </div>
</template>

<script>
const skillColors = {
  data: '#2196f3',
  devops: '#8561c5',
  'misc-programming': '#009688',
};

export default {
  name: 'HomeSkillProgressSection',
  props: { skills: { type: Uint8Array }, title: { type: String } },
  data() {
    return { skillColors };
  },
};
</script>

<style scoped>
.home-skills-progress-section {
  font-size: 0.8rem !important;
  width: 250px;
}
</style>
