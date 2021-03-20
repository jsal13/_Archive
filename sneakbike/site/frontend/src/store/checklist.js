const duties = {
  P1: {
    "Before Race Day": ["Have dev tools setup (Terraform, AWSCLI, OBS, VLC, ...)", "Have Sneakops OBS Profile"],
    "Race Day": [
      "<code>terraform apply</code> the server up",
      "Give each runner the RTMP address and their keys",
      "Use VLC Media Source to capture each runner's Stream",
      "Pick Background music, if necessary",
      "Check background audio: make sure the background music or game sound starts (and stays) in the upper-green section of the OBS mixer",
      "Test C1 and C2 levels above the music / game audio, as well as relative to each other",
      "Share the live OBS screen with C1 and C2",
    ],
    "During Race": [
      "Shut off a runner's feed when the runner is finished with the race",
    ],
    "After Race": ["Stop Streaming to the Sneakbike channel", "<span style=\"color: #e31616;\">SHUT DOWN SERVER WITH <code>terraform destroy</code>!</span>"],
  },
  P2: { "Race Day": [] },
  C1: {
    "Before Race Day": ["Test the games in the ZIP file to make sure they're all correct", "Check the README for glaring errors or typos"],
    "Race Day": ["Have the canned opening and closing ready to read off."],
    "During Race": [
      "Shout out racers, host, main mod or mods, and commentators.",
    ],
    // "After Race": [],
  },
  C2: {
    "Before Race Day": [
      "Test the games in the Zip file to make sure they're all correct.", "Check the README for glaring errors or typos"
    ],
    "Race Day": ["Mute each runner's audio when the race is to begin (you'll be told when to do so by P1 or C1)",],
    "During Race": [
      "Unmute runners when doing runner interviews",
      "Find a raid when it gets close to the end (probably when the runners get into the post-race room)",

    ],
    // "After Race": [],
  },
  GP1: {
    "Before Race Day": [
      "Choose console and games",
      "Pick Objectives for games",
      "Validate game and objective choices with commenatators",
      "Once validated with commenators, use the README Generator to generate a readme for the runners",
      "Rename the games 'Game_1', 'Game_2', etc., and zip them in a folder with the README",
      "Send the zip file to the commentators",
    ],
  },
  M1: {
    // "Before Race Day": [],
    "Race Day": ["Update Nightbot Commands"],
    "During Race": ["Moderate Chat"],
    // "After Race": [],
  },
  "??": {
    "Who Knows When?": ["Check that each runner has a functioning OBS with Sneakbike profile",
      "Check that each runner has a functioning Emulator for the relevant system",
      "Check that each runner has configured their controller correctly by having them run a test game",]
  }
};

export default {
  namespaced: true,
  state: {
    duties: duties
  },
}