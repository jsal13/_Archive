<template>
  <div class="home-apps-card">
    <div class="card" style="width: 250px;">
      <router-link :to="link">
        <img :src="image" class="card-img-top" :alt="title" width="200" />
      </router-link>
      <div class="card-body">
        <h5 class="card-title">
          <router-link :to="link">{{ title }}</router-link>
        </h5>
        <p class="card-text">{{ description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeAppsCard',
  props: {
    image: { type: String },
    description: { type: String },
    alt: { type: String },
    title: { type: String },
    link: { type: String },
  },
};
</script>

<style scoped>
.card-text {
  font-size: 0.75rem;
}

img {
  border: 1px solid #2196f3;
}
</style>
