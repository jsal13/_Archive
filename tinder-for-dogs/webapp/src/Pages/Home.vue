<template>
  <div>
    <Vue2InteractDraggable
      v-if="isShowing"
      @draggedRight="draggedRight"
      :interact-max-rotation="15"
      :interact-out-of-sight-x-coordinate="500"
      :interact-x-threshold="200"
    >
      <div class="card">
        <img class="card__image" alt="test-img" src="../assets/dachshund-winking.jpg" />
        <h3>Drag me!</h3>
      </div>
    </Vue2InteractDraggable>
  </div>
</template>

<script>
import { Vue2InteractDraggable } from "vue2-interact";

export default {
  name: "Home",
  components: {
    Vue2InteractDraggable
  },
  data() {
    return {
      isShowing: true
    };
  },
  methods: {
    // Placeholder
    draggedRight() {
      this.isShowing = false;

      setTimeout(() => {
        this.isShowing = true;
      }, 1000);
    }
  }
};
</script>

<style>
.card__image {
  max-height: 300px;
}
</style>
