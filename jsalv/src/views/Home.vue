<template>
  <div class="home-text">
    <v-container class="mt-4">
      <v-container class="mb-5">
        <v-row>
          <v-col class="col-10 offset-1">
            <h1 class="text-h1 text-right">
              Hello.
              <br />I'm
              <span class="primary--text">James</span>.
            </h1>
          </v-col>
        </v-row>
      </v-container>

      <v-container>
        <v-row>
          <v-col class="col-10 offset-1">
            <div class="hook-line">
              <img
                alt="Hello there!"
                src="@/assets/images/jsal_standing.png"
                height="64px"
                width="64px"
                class="mb-1"
              />
              <p>
                I studied
                <a
                  href="https://en.wikipedia.org/wiki/Algebraic_topology"
                  target="_blank"
                >math</a> for a while, and now I work with a bunch of data trying to learn new things and solve hard problems.
                Sometimes I'm successful.
              </p>
              <p>
                I started learning C# and Unity for Game Development while on break, here's some of the <a href="https://melat0nin.itch.io" target="_blank">gamejam games</a> that I made.  Not great, but, you know, baby steps!  Larger games are in-progress.  :']
              </p>
              <p>
                I used to run a retro game racing charity called
                <a href="https://twitch.tv/sneakbike" target="_blank">Sneakbike</a> with the help of some good pals.  Check out some of the vods <a href="https://www.youtube.com/channel/UC5WLNGgGQH2tpNHM5uk2kCg" target="_blank">here</a>.
              </p>
            </div>
          </v-col>
        </v-row>
      </v-container>
      <hr />
      <home-skills />
    </v-container>
  </div>
</template>

<script>
import HomeSkills from '@/components/HomeSkills.vue';

export default {
  name: 'Home',
  components: { HomeSkills },
};
</script>

<style scoped>
.hook-line > img,
hook-line > p {
  float: left;
  align-items: baseline;
}
</style>
