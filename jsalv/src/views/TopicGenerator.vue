<template>
  <div class="topic-generator">
    <v-card class="mx-auto container" max-width="500">
      <v-card-text>
        <v-row align="center" class="mb-5">
          <v-col>
            <span class="topics">{{ currentTopic }}</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6">
            <v-btn @click="GenerateTopic">Generate New Topic</v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import wordList from '@/data/wordList';

export default {
  name: 'TopicGenerator',
  data() {
    return {
      wordList,
      currentTopic: '',
      wordsLength: null,
    };
  },
  created() {
    this.wordsLength = this.wordList.length;
    this.GenerateTopic();
  },
  methods: {
    GenerateTopic() {
      const randWords = [];
      const numWords = 2 + Math.floor(Math.random() * 2);

      for (let idx = 0; idx < numWords; idx += 1) {
        const r = Math.floor(Math.random() * this.wordsLength);

        randWords.push(this.wordList[r].trim());
      }
      this.currentTopic = randWords.join(' ');
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
}

.topics {
  font-size: 1.5rem;
}
</style>
