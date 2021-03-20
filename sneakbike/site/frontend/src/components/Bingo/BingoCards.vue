<template>
  <div class="bingo-card">
    <div class="grid-container">
      <BingoCard v-for="(item, index) in bingoValues" :key="index" :cardBGColor="cardBGColor">
        <span class="noselect">{{ item }}</span>
      </BingoCard>
    </div>

    <br />
    <br />

    <div class="color-picker">
      <input
        type="button"
        class="color-button"
        v-for="(k, value, index) in colorButtons"
        :key="index"
        :style="{ backgroundColor: k }"
        v-on:click="setCardBGColor(k)"
      />
    </div>

    <div class="share-seed">
      <p>
        Share Link:
        <a
          :href="
            currentURL.includes('?seed') ? currentURL : currentURL + '?seed=' + bingoCardSignature
          "
        >
          {{
          currentURL.includes("?seed") ? currentURL : currentURL + "?seed=" + bingoCardSignature
          }}
        </a>
      </p>
    </div>
  </div>
</template>

<script>
import getBingoCardValues from "./getBingoCardValues";
import BingoCard from "./BingoCard.vue";

const colorButtons = {
  cardinalRed: "#BD2031",
  hotPink: "#FF69B4",
  darkOrange: "#FF8C00",
  gold: "#FFD700",
  canaryYellow: "#ffef00",
  papayawhip: "#ffefd5",
  seaGreen: "#2F7D55",
  blue: "#5b92f8",
  ultramarineBlue: "#4166f5",
  darkPurple: "#6E2AF9",
  mediumPurple: "#9370DB",
};

export default {
  name: "BingoCards",
  components: { BingoCard },
  data() {
    return {
      cardBGColor: "#5b92f8",
      colorButtons,
      bingoCardDict: { bingoCard: null, signature: null },
    };
  },
  mounted() {
    this.startPage();
  },
  computed: {
    bingoValues() {
      if (this.bingoCardDict.bingoCard !== null) {
        return this.bingoCardDict.bingoCard.flat();
      }
      return null;
    },
    bingoCardSignature() {
      return this.bingoCardDict.signature;
    },
    currentURL() {
      return window.location.href;
    },
  },
  methods: {
    setCardBGColor(val) {
      this.cardBGColor = val;
    },

    startPage() {
      this.bingoCardDict = getBingoCardValues();
    },
  },
};
</script>

<style scoped>
.grid-container {
  grid-template-columns: repeat(5, minmax(125px, 175px));
  grid-template-rows: repeat(5, 125px);
  display: grid;
  grid-gap: 1px 1px;
  justify-content: center;
}

.color-button {
  display: inline-flex;
  width: 50px;
  height: 35px;
  border-radius: 5px;
  align-items: center;
  padding-left: 10px;
  margin-left: 4px;
}

.color-picker {
  display: flex;
  align-items: center;
  justify-content: center;
}

.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently
                        supported by Chrome, Edge, Opera and Firefox */
}

.share-seed {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2em;
  font-family: "Roboto", sans-serif;
  padding: 0.5em;
}
</style>
