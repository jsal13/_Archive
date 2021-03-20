<template>
  <div class="hkr-countdown-timer">
    <v-row justify="space-around">
      <v-col cols="10" offset="1">
        <v-card outlined class="pa-1" max-width="325">
          <v-list-item two-line>
            <v-list-item-content>
              <div class="overline mb-4">Tracker will be displayed in:</div>
              <v-list-item-title class="headline mb-1">{{secondsRemaining}} minutes</v-list-item-title>
              <v-list-item-subtitle class="mt-10">
                <v-btn @click="stopTimerAndEmitFinished">Display Tracker Now</v-btn>
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "HKRCountdownTimer",
  data() {
    return { timerInterval: null, startTime: null, elapsedTime: null };
  },
  props: {
    timeLimitMinutes: Number,
  },
  methods: {
    updateTime() {
      var now = new Date().getTime();
      this.elapsedTime = now - this.startTime;

      if (this.secondsRemaining <= 0) {
        this.stopTimerAndEmitFinished();
      }
    },
    stopTimerAndEmitFinished() {
      window.clearInterval(this.timerInterval);
      this.$emit("timerFinished");
    },
  },
  computed: {
    secondsRemaining() {
      return this.timeLimitMinutes - Math.floor(this.elapsedTime / 60000);
    },
  },
  mounted() {
    // Update every minute, approximately.
    this.timerInterval = window.setInterval(() => {
      this.updateTime();
    }, 5000);
  },
  created() {
    this.startTime = new Date().getTime();
  },
};
</script>
