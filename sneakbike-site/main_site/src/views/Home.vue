<template>
  <div class="home">
    <h2 class="title-text"> &gt; sneakbike</h2>
    <h3 class="title-text"> &gt; more coming soon</h3>

    <video playsinline autoplay muted loop id="helma_background">
      <source src="@/assets/helma_background.mp4" type="video/mp4"/>
    </video>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style scoped>
video {
  object-fit: cover;
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;
}

.title-text {
  color: #f0f0f0;
  z-index: 20;
  position: relative;
  left: 2vw;
  top: 2vh;

}
</style>
