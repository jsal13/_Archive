<template>
  <div>
    <div class="loc-div" :style="styleLocDiv">
      <div class="loc-circle" :style="styleLocCircle">
        <div class="loc-title-div">
          <span class="loc-title-text">{{ arrayLocDataObj[loc]['abbr'] }}</span>
        </div>
      </div>
      <div class="item-div">
        <v-flex class="d-flex flex-wrap">
          <div v-for="(item, name, jdx) in distinctItems" :key="`${item}-${jdx}`">
            <tracker-image
              :item="item"
              :name="name"
              :width="40"
              :height="40"
              @itemToggled="isRectangleClear"
              class="tracker-image"
            />
          </div>
        </v-flex>
      </div>
    </div>
  </div>
</template>
<script>
import TrackerImage from "@/components/HollowKnight/TrackerImage.vue";
import { mapState } from "vuex";

export default {
  name: "HKRItemRect",
  components: { TrackerImage },
  props: {
    loc: String,
    zindex: Number,
  },
  computed: {
    ...mapState("hkr", ["itemFoundState", "arrayLocDataObj"]),
    styleLocDiv() {
      return `background-color: ${this.arrayLocDataObj[this.loc].background}; 
      border: 6px solid ${this.arrayLocDataObj[this.loc].border};
      width: ${80 + this.arrayLocDataObj[this.loc]["items"].length * 41}px;`;
    },
    styleLocCircle() {
      return `background-color: ${this.arrayLocDataObj[this.loc].border};
      border: 2px solid ${this.arrayLocDataObj[this.loc].border};`;
    },
    distinctItems() {
      const eItems = {};
      for (var i = 0; i < this.arrayLocDataObj[this.loc]["items"].length; i++) {
        eItems[
          `${this.arrayLocDataObj[this.loc]["abbr"]}-${
            this.arrayLocDataObj[this.loc]["items"][i]
          }-${i}`
        ] = this.arrayLocDataObj[this.loc]["items"][i];
      }
      return eItems;
    },
  },
  methods: {
    emitHideRow() {
      this.$emit("hideRow");
    },
    isRectangleClear() {
      const allHidden = Object.keys(this.distinctItems).every(
        (x) => this.itemFoundState[x]
      );
      if (allHidden) {
        this.emitHideRow();
      }
    },
  },
};
</script>

<style lang="scss" scoped>
$height: 62px;
$large-radius: 4rem;
$item-starting-offset-left: 65px;
$item-starting-offset-top: 3px;

.loc-div {
  position: relative;
  height: $height;
  border-radius: $large-radius;
}
.loc-circle {
  position: absolute;
  width: $height + 6px;
  height: $height - 0px;
  top: -6px;
  left: -6px;
  border-top-left-radius: $large-radius;
  border-bottom-left-radius: $large-radius;
  padding: 0;
  margin: 0;
}

.loc-title-div {
  position: absolute;
  left: 15px;
  top: 13px;
}
.loc-title-text {
  font-family: "Roboto", sans-serif;
  font-size: 1rem;
  font-weight: 500;
  color: white;
  -webkit-user-select: none; /* Safari */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* IE10+/Edge */
  user-select: none; /* Standard */
  cursor: default;
}

.item-div {
  position: absolute;
  left: $item-starting-offset-left;
  top: $item-starting-offset-top;
}
</style>