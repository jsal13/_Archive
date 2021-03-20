<template>
  <div class="home">
    <div class="sneakbike-description">
      <v-container>
        <v-row>
          <v-col cols="10" offset="1">
            <h1>
              What
              <i>is</i> Sneakbike?
            </h1>
            <p>Sneakbike is a community of people working towards two primary goals:</p>

            <ul class="pt-1 pb-4">
              <li class="pb-1">
                <b>Community</b>: Making friends, being nice to each other, and friendly competition.
              </li>
              <li class="pb-1">
                <b>Learning New Skills</b>: A commitment to helping each other grow and learn new things.
              </li>
            </ul>
            <v-parallax
              src="@/assets/backgrounds/bkgd_helma_cropped_pad.png"
              class="ma-4 mb-10"
              width="100%"
              height="200"
            />

            <h1>What does Sneakbike do?</h1>

            <p>
              The Sneakbike Community currently hosts two different events:
              <i>Sneakbike Mystery Races</i> and
              <i>Sneakly Weeklys</i>.
            </p>

            <div class="ml-6 mt-6">
              <h2>Sneakbike Mystery Races</h2>
              <p>
                Mystery Races are events where
                <b>
                  four similarly-skilled players
                  race to
                  complete an objective in each of two or three "mystery games"
                </b>
                which are only revealed to the runners a few minutes before the race starts!
              </p>
            </div>

            <div class="ml-6 mt-6">
              <h2>Sneakly Weeklys</h2>
              <p>
                This is the Sneakbike Community's "anything goes" event. It's a good time
                to
                <b>try out some new event ideas or to have a community night</b>.
              </p>

              <p>
                In the past we've had
                <i>
                  non-mystery races, casual playthroughs of weird
                  games, learning a speedrun together, teaching streams, learning randomizer games, hollow knight randomizer bingo,
                </i> and sometimes we just hang out and play games together.
              </p>
            </div>

            <h2 class="mt-6">What's the Sneakbike Toolkit?</h2>
            <p>
              The Sneakbike Toolkit (SBTK) is our lightweight, open-source solution to having a
              number of individuals stream on the same stream. It allows us to easily
              host races with a number of runners. To use or play around with the code, check out
              <a
                href="https://github.com/jsal13/sneakbike/"
              >our github.</a>
            </p>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>
