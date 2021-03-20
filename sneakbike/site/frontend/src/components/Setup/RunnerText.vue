<template>
  <div class="setup-runner-text">
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1>Runner Setup</h1>
          <div class="ml-6 mt-6">
            <p>
              <b>Before you begin...</b>
            </p>

            <ul class="pt-1 pb-4">
              <li
                class="pb-2"
              >We assume you're running Windows 10. If not, check in with us and we'll get you compatible software.</li>
              <li class="pb-2">
                If you'd rather see the video tutorial, that's available
                <a
                  href="https://www.youtube.com/watch?v=qtB0n4RuBGo"
                  target="_blank"
                >here</a>.
              </li>
            </ul>

            <div class="ml-6 mt-6">
              <h2>Getting the EmuHawk (BizHawk) Emulator</h2>

              <p>In order to emulate retro games, we use the EmuHawk Emulator in the BizHawk suite of tools. If you find there are issues with this (eg, controller acting strangely, etc.) please let us know in the discord and we'll help you debug.</p>

              <ol class="pt-1 pb-4">
                <li class="pb-2">
                  Download the
                  <a
                    href="https://github.com/TASVideos/BizHawk-Prereqs/releases"
                    target="_blank"
                  >bizhawk_prereqs ZIP file</a>, which is listed under
                  <code>Assets</code>. After downloading, unzip and install.
                </li>
                <li class="pb-2">
                  Download
                  <a
                    href="https://github.com/TASVideos/BizHawk/releases"
                    target="_blank"
                  >Bizhawk</a>, which is listed under
                  <code>Assets</code> and looks something like
                  <code>Bizhawk-Numbers.zip</code> (similar to the image below).
                  <b>Unzip the file once it has downloaded</b>.
                  <img src="@/assets/setup/bizhawk_download.png" alt="Bizhawk Download" />
                  <warning-card>
                    There is currently an issue where Windows 10 thinks that BizHawk is a virus.
                    <b>This is a false positive.</b> Try downloading
                    <a
                      href="https://github.com/TASVideos/BizHawk/releases/tag/2.4.2"
                      target="_blank"
                    >Version 2.4.2</a> if your Windows refuses to let you open the latest.
                  </warning-card>
                </li>
                <li class="pb-2">
                  In the unzipped Bizhawk folder, you'll find a program called
                  <code>EmuHawk.exe</code>. This is the emulator and you can double-click to run it.
                </li>
              </ol>
            </div>
            <div class="ml-6 mt-6">
              <h2>Configuring the EmuHawk Emulator</h2>
              <info-card>
                If you'd rather see the video of the config, check our
                <a
                  href="https://youtu.be/J_WM3zYQVH0"
                  target="_blank"
                >video tutorial</a>.
              </info-card>

              <p>We'llconfigure three things in BizHawk.</p>
              <ul class="pt-1 pb-4">
                <li class="pb-2">Hotkeys</li>
                <li class="pb-2">Display</li>
                <li class="pb-2">Sound</li>
              </ul>

              <p>
                Each of these items can be found in the
                <code>Config</code> menu at
                the top of the EmuHawk program. The screenshots below show you what each screen should look
                like.
                <i>
                  For the Sound menu, if you uncheck the box we've circled in red,
                  this will mute the emulator. Note that your sound device might be different than in the image.
                </i>
              </p>

              <img src="@/assets/console_config/emuhawk_hotkeys_config.png" />
              <img src="@/assets/console_config/emuhawk_SNES_display_config.png" />
              <img src="@/assets/console_config/emuhawk_sound_config.png" />
            </div>

            <div class="ml-6 mt-6">
              <h2>Setting Up OBS</h2>

              <p>OBS is what we use to stream the game to the Sneakbike server (and what many people use to stream to Twitch).</p>

              <ol class="pt-1 pb-4">
                <li class="pb-2">
                  Download and install
                  <a href="https://obsproject.com/" target="_blank">OBS</a>.
                </li>
                <li class="pb-2">
                  Download the
                  <a
                    href="https://drive.google.com/file/d/16uHzUpr4XAinq1Do_KP3-I_ptS1bJCrB/view?usp=sharing"
                    target="_blank"
                  >Sneakbike Profile for OBS</a>.
                  <b>Unzip this once it is downloaded.</b>
                </li>
              </ol>

              <p>To import this profile, follow the directions below, using the gif below as a guide if you need to.</p>
              <img src="@/assets/setup/sneakbike_import_profile.gif" alt="OBS Profile Import" />

              <ol class="pt-1 pb-4">
                <li class="pb-2">
                  In OBS, Go into
                  <code>Profile > Import</code>, navigate to the unzipped Sneakbike folder from the previous steps, click the
                  <code>Sneakbike_Profile</code> folder and hit "open".
                </li>

                <li class="pb-2">
                  Still in OBS, go into the
                  <code>Profile</code> menu again. You should see (at least) two profiles at the bottom, including
                  <code>Sneakbike</code>.
                </li>
                <li>
                  <ul class="pt-1 pb-1">
                    <li class="pb-2">
                      Clicking on
                      <code>Sneakbike</code> will bring you to the Sneakbike profile we
                      require for racers.
                    </li>
                    <li class="pb-2">
                      You can click the original Profile (usually called
                      <code>Untitled</code>) to go back to your normal streaming profile, if you had one.
                    </li>
                  </ul>
                </li>
              </ol>
            </div>

            <div class="ml-6 mt-6">
              <h2>Racing</h2>
              <p>Before the race, usually the day-of, we'll give you instructions on how to stream to the correct location and how to set up a scene to have your gameplay broadcast correctly. Don't worry about it for now, but if you're interested ask us in the discord!</p>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "SetupRunnerText",
};
</script>