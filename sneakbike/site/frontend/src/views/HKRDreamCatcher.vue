<template>
  <div>
    <div v-if="!spoilerRetrieved">
      <v-row>
        <v-col cols="10" offset="1">
          <h2>Hollow Knight Randomizer "Quick Seed" Tool</h2>
          <p>This tool allows for a "quick play" seed by showing the location of important items and abilities. You may customize what is shown below with "Show Item Options".</p>

          <p>Thanks to BearsAndBeets for design and color help and the Sneakbike Community for various ideas and improvements.</p>

          <hr />
          <br />
          <h2>Quickstart</h2>
          <p>
            <b>Pick what things you want displayed in "Show Item Options". Then upload your Hollow Knight Randomizer Spoiler below. This is usually located (on Windows) at:</b>
          </p>

          <p>
            <code>C:\Users\yourname\AppData\LocalLow\Team Cherry\Hollow Knight\RandomizerSpoilerLog.txt</code>
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="10" offset="1">
          <v-expansion-panels>
            <HKRItemToggle :allowBlueMode="false" />
          </v-expansion-panels>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6" offset-sm="2">
          <v-file-input
            truncate-length="120"
            accept=".txt"
            label="File input"
            @change="onFileChange"
          />
        </v-col>
        <v-col cols="2">
          <v-btn :disabled="spoiler_txt.length === 0" @click="submitSpoilerAndPrepareTracker">Submit</v-btn>
        </v-col>
      </v-row>
    </div>

    <div v-if="spoilerRetrieved" class="tracker-page">
      <v-col cols="10" offset="1">
        <v-tooltip transition="slide-x-transition" right :open-delay="500">
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon @click="hideOptions = !hideOptions" v-bind="attrs" v-on="on">
              <v-icon>{{ hideOptions ? 'mdi-chevron-up' : 'mdi-chevron-down'}}</v-icon>
            </v-btn>
          </template>
          <span>Toggle Options Menu</span>
        </v-tooltip>

        <v-expansion-panels v-show="hideOptions">
          <HKRItemToggle :allowSetTimer="false" />
          <HKRPills />
        </v-expansion-panels>
      </v-col>

      <v-col cols="10" offset="1">
        <HKRItemTable v-if="showTracker" />
        <HKRCountdownTimer
          v-if="!showTracker"
          :timeLimitMinutes="timerValue"
          @timerFinished="showTracker = !showTracker"
        />
      </v-col>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapState, mapMutations } from "vuex";
import HKRItemTable from "@/components/HollowKnight/HKRItemTable.vue";
import HKRItemToggle from "@/components/HollowKnight/HKRItemToggle.vue";
import HKRPills from "@/components/HollowKnight/HKRPills.vue";
import HKRCountdownTimer from "@/components/HollowKnight/HKRCountdownTimer.vue";

export default {
  name: "HKRDreamCatcher",
  components: { HKRItemToggle, HKRItemTable, HKRPills, HKRCountdownTimer },
  data: function () {
    return {
      spoiler_txt: "",
      spoilerRetrieved: false,
      hideOptions: false,
      showTracker: true,
    };
  },
  computed: {
    ...mapState("hkr", [
      "showDreamers",
      "showAbilities",
      "showUsefulItems",
      "timerValue",
      "arrayDreamers",
      "arrayAbilities",
      "arrayUsefulItems",
      "arrayLocDataObj",
    ]),
  },
  methods: {
    ...mapMutations("hkr", [
      "toggleDreamers",
      "toggleAbilities",
      "toggleUsefulItems",
      "setArrayDreamers",
      "setArrayAbilities",
      "setArrayUsefulItems",
      "setTimer",
      "defineLocObject",
    ]),
    onFileChange(file) {
      if (!(file.size || file.name === "RandomizerSpoilerLog.txt")) return;
      this.createText(file);
    },
    createText(file) {
      var reader = new FileReader();
      reader.readAsText(file);
      reader.onload = (e) => {
        this.spoiler_txt = e.target.result;
      };
    },
    submitSpoilerAndPrepareTracker() {
      axios
        .post(`${process.env.VUE_APP_API_LOCATION}/hkr/uploadspoiler/`, {
          files: this.spoiler_txt,
        })
        .then((response) => {
          const resp = response["data"];
          this.setArrayDreamers({ value: resp["dreamers"] });
          this.setArrayAbilities({ value: resp["abilities"] });
          this.setArrayUsefulItems({ value: resp["useful_items"] });
          this.defineLocObject();

          // If there's a timer, don't show the tracker yet.
          this.showTracker = this.timerValue === 0;
          this.spoilerRetrieved = true;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  mounted() {
    // temp
    this.spoiler_txt = `
Randomization completed with seed: 732952683

PROGRESSION ITEMS
(4) Dashmaster<---at--->Sly
(6) Crossroads Stag<---at--->Vengeful Spirit
(8) Crystal Heart<---at--->Grubsong
(10) Shade Cloak<---at--->Iselda
(12) Howling Wraiths<---at--->Hallownest Seal-Fog Canyon West
(14) Queen's Gardens Stag<---at--->85 Geo-Greenpath Chest
(16) City Storerooms Stag<---at--->Dashmaster
(18) Grubberfly's Elegy<---at--->Hallownest Seal-Fungal Wastes Sporgs
(19) King's Brand<---at--->Soul Catcher
(22) Abyss Shriek<---at--->Thorns of Agony
(23) Elegant Key<---at--->Mask Shard-Brooding Mawlek
(31) Descending Dark<---at--->City Storerooms Stag
(34) Mothwing Cloak<---at--->Fury of the Fallen
(35) Lurien<---at--->King's Idol-Grubs
(36) Simple Key-City<---at--->Rancid Egg-Queen's Gardens
(39) Greenpath Stag<---at--->Rancid Egg-Waterways West Bluggsac
(40) Isma's Tear<---at--->Wanderer's Journal-Ancient Basin
(42) Shade Soul<---at--->Simple Key-Basin
(45) Lumafly Lantern<---at--->Rancid Egg-Waterways Main
(51) Mantis Claw<---at--->Dreamshield
(52) Hidden Station Stag<---at--->Wanderer's Journal-King's Station
(55) Stag Nest Stag<---at--->Vessel Fragment-City
(56) Vengeful Spirit<---at--->Wanderer's Journal-Cliffs
(58) Cyclone Slash<---at--->Vessel Fragment-Stag Nest
(62) Great Slash<---at--->Mask Shard-Stone Sanctuary
(66) Grimmchild<---at--->Queen's Gardens Stag
(67) Desolate Dive (1)<---at--->Grimmchild
(68) Lifeblood Core<---at--->380 Geo-Soul Master Chest
(69) Monomon<---at--->Rancid Egg-Upper Kingdom's Edge
(70) Sprintmaster<---at--->Rancid Egg-Waterways East
(71) Tram Pass<---at--->Pale Ore-Basin
(74) Glowing Womb<---at--->Shade Cloak
(83) Dash Slash<---at--->Isma's Tear
(84) Desolate Dive<---at--->Descending Dark
(89) Sharp Shadow<---at--->Arcane Egg-Shade Cloak
(104) Dream Nail<---at--->Hallownest Seal-Deepnest By Mantis Lords
(108) Simple Key-Lurker<---at--->Pale Ore-Seer
(110) Simple Key-Sly<---at--->Dream Gate
(113) Simple Key-Basin<---at--->Weaversong
(114) Isma's Tear (1)<---at--->Rancid Egg-City of Tears Pleasure House
(116) Vengeful Spirit (1)<---at--->Godtuner
(118) Queen's Station Stag<---at--->Hallownest Seal-Queen's Gardens
(119) Shopkeeper's Key<---at--->Sharp Shadow
(121) Spore Shroom<---at--->Glowing Womb
(122) Love Key<---at--->Pale Ore-Nosk
(128) Dirtmouth Stag<---at--->Grubberfly's Elegy
(129) Lifeblood Heart<---at--->Shape of Unn
(130) King Fragment<---at--->King's Idol-Great Hopper
(131) Resting Grounds Stag<---at--->Wanderer's Journal-Crystal Peak Crawlers
(132) Mothwing Cloak (1)<---at--->Shade Soul
(134) Monarch Wings (1)<---at--->Rancid Egg-Weaver's Den
(135) Mantis Claw (1)<---at--->Charm Notch-Fog Canyon
(140) City Crest<---at--->Pale Ore-Colosseum
(143) King's Station Stag<---at--->Wanderer's Journal-Pleasure House
(144) Howling Wraiths (1)<---at--->Rancid Egg-Waterways West Pickup
(145) Mark of Pride<---at--->Mark of Pride
(147) Weaversong<---at--->Awoken Dream Nail
(153) Monarch Wings<---at--->Mask Shard-Seer
(154) Dreamer (1)<---at--->Hallownest Seal-Queen's Station
(156) Shade Cloak (1)<---at--->Lifeblood Core
(160) Herrah<---at--->Hallownest Seal-Watcher Knight
(162) Distant Village Stag<---at--->655 Geo-Watcher Knights Chest
(164) Dream Nail (1)<---at--->Mask Shard-Deepnest
(165) Void Heart (1)<---at--->Rancid Egg-Fungal Core
(168) Crystal Heart (1)<---at--->Hallownest Seal-King's Station
(169) Void Heart<---at--->Rancid Egg-Crystal Peak Tall Room
(171) Awoken Dream Nail<---at--->Void Heart
(172) Dream Gate<---at--->King's Idol-Crystal Peak
(173) Queen Fragment<---at--->King Fragment
(175) Joni's Blessing<---at--->Rancid Egg-City of Tears Left

ALL ITEMS

Forgotten Crossroads:
(1) Rancid Egg-Beast's Den<---at--->200 Geo-False Knight Chest
(3) Mask Shard-Sly4<---at--->Pale Ore-Grubs
(5) 160 Geo-Weavers Den Chest<---at--->City Crest
(7) Mask Shard-Stone Sanctuary<---at--->Crossroads Stag
(8) Crystal Heart<---at--->Grubsong
(23) Elegant Key<---at--->Mask Shard-Brooding Mawlek
(27) Pale Ore-Crystal Peak<---at--->Vessel Fragment-Crossroads
(35) Lurien<---at--->King's Idol-Grubs
(43) Rancid Egg-Upper Kingdom's Edge<---at--->Rancid Egg-Grubs
(44) Pale Ore-Colosseum<---at--->Mask Shard-5 Grubs
(59) Hallownest Seal-Greenpath<---at--->Hallownest Seal-Grubs
(77) Mask Shard-Enraged Guardian<---at--->Mask Shard-Crossroads Goam
(121) Spore Shroom<---at--->Glowing Womb
(125) Fragile Strength<---at--->Hallownest Seal-Crossroads Well
(128) Dirtmouth Stag<---at--->Grubberfly's Elegy

Dirtmouth:
(2) Rancid Egg-Weaver's Den<---at--->Dirtmouth Stag
(67) Desolate Dive (1)<---at--->Grimmchild
(82) Rancid Egg-Fungal Core<---at--->Mask Shard-Bretta
(126) Rancid Egg-Dark Deepnest<---at--->Charm Notch-Grimm
(139) Wanderer's Journal-Kingdom's Edge Camp<---at--->Nailmaster's Glory

(4) Sly:
Dashmaster
Arcane Egg-Seer
Wanderer's Journal-Crystal Peak Crawlers
Rancid Egg-Waterways Main
Wanderer's Journal-Resting Grounds Catacombs
620 Geo-Mantis Lords Chest
Fury of the Fallen

Ancestral Mound:
(6) Crossroads Stag<---at--->Vengeful Spirit
(19) King's Brand<---at--->Soul Catcher

(9) Salubra:
Quick Slash
Wanderer's Journal-Kingdom's Edge Requires Dive
Mask Shard-Waterways
Godtuner
Grubsong
Mask Shard-Seer
Rancid Egg-Waterways West Bluggsac

(10) Iselda:
Shade Cloak
Shape of Unn
Mask Shard-Bretta
Gathering Swarm
Mask Shard-Queen's Station
King's Idol-Glade of Hope
Mask Shard-Grey Mourner

Greenpath:
(11) Stalwart Shell<---at--->Greenpath Stag
(14) Queen's Gardens Stag<---at--->85 Geo-Greenpath Chest
(20) Thorns of Agony<---at--->Wanderer's Journal-Greenpath Stag
(22) Abyss Shriek<---at--->Thorns of Agony
(24) Wanderer's Journal-Cliffs<---at--->Mothwing Cloak
(25) Hallownest Seal-Fog Canyon West<---at--->Hallownest Seal-Greenpath
(73) Rancid Egg-Crystal Peak Dive Entrance<---at--->Rancid Egg-Sheo
(75) Vessel Fragment-Sly1<---at--->Vessel Fragment-Greenpath
(101) Hallownest Seal-Watcher Knight<---at--->Wanderer's Journal-Greenpath Lower
(138) Rancid Egg-City of Tears Left<---at--->Great Slash

Fog Canyon:
(12) Howling Wraiths<---at--->Hallownest Seal-Fog Canyon West
(41) Charm Notch-Fog Canyon<---at--->Hallownest Seal-Fog Canyon East
(135) Mantis Claw (1)<---at--->Charm Notch-Fog Canyon

(13) Leg Eater:
Mask Shard-Brooding Mawlek
Wanderer's Journal-Kingdom's Edge Entrance
King's Idol-Deepnest
Vessel Fragment-Greenpath
King's Idol-Pale Lurker
Hallownest Seal-Queen's Station
Rancid Egg-City of Tears Pleasure House

Mantis Village:
(15) Vessel Fragment-Deepnest<---at--->Mantis Claw
(16) City Storerooms Stag<---at--->Dashmaster
(90) Pale Ore-Seer<---at--->Hallownest Seal-Mantis Lords
(145) Mark of Pride<---at--->Mark of Pride
(148) Arcane Egg-Shade Cloak<---at--->620 Geo-Mantis Lords Chest

Fungal Wastes:
(17) Hallownest Seal-Deepnest By Mantis Lords<---at--->Charm Notch-Shrumal Ogres
(18) Grubberfly's Elegy<---at--->Hallownest Seal-Fungal Wastes Sporgs
(133) Rancid Egg-Blue Lake<---at--->Wanderer's Journal-Above Mantis Village
(142) 80 Geo-Crystal Peak Chest<---at--->Spore Shroom
(149) Wanderer's Journal-City Storerooms<---at--->Wanderer's Journal-Fungal Wastes Thorns Gauntlet

Howling Cliffs:
(21) Quick Focus<---at--->Baldur Shell
(56) Vengeful Spirit<---at--->Wanderer's Journal-Cliffs
(57) Vessel Fragment-Basin<---at--->King's Idol-Cliffs
(61) 150 Geo-Resting Grounds Chest<---at--->Cyclone Slash
(63) Arcane Egg-Birthplace<---at--->Joni's Blessing

Queen's Station:
(26) Wanderer's Journal-Ancient Basin<---at--->Queen's Station Stag
(88) Deep Focus<---at--->Mask Shard-Queen's Station
(154) Dreamer (1)<---at--->Hallownest Seal-Queen's Station

City of Tears:
(28) Rancid Egg-Sheo<---at--->Simple Key-City
(29) Soul Catcher<---at--->Hallownest Seal-City Rafters
(30) Rancid Egg-Waterways West Pickup<---at--->Wanderer's Journal-City Storerooms
(31) Descending Dark<---at--->City Storerooms Stag
(132) Mothwing Cloak (1)<---at--->Shade Soul
(155) Rancid Egg-Crystal Peak Dark Room<---at--->Lurien
(160) Herrah<---at--->Hallownest Seal-Watcher Knight
(162) Distant Village Stag<---at--->655 Geo-Watcher Knights Chest
(175) Joni's Blessing<---at--->Rancid Egg-City of Tears Left

Crystal Peak:
(32) Wayward Compass<---at--->Rancid Egg-Crystal Peak Dive Entrance
(33) Wanderer's Journal-Greenpath Stag<---at--->Rancid Egg-Crystal Peak Dark Room
(94) King's Idol-Crystal Peak<---at--->Deep Focus
(103) Wanderer's Journal-Greenpath Lower<---at--->80 Geo-Crystal Peak Chest
(115) Spell Twister<---at--->Shopkeeper's Key
(123) Hallownest Seal-Mantis Lords<---at--->Crystal Heart
(131) Resting Grounds Stag<---at--->Wanderer's Journal-Crystal Peak Crawlers
(167) Vessel Fragment-City<---at--->Mask Shard-Enraged Guardian
(169) Void Heart<---at--->Rancid Egg-Crystal Peak Tall Room
(172) Dream Gate<---at--->King's Idol-Crystal Peak

King's Pass:
(34) Mothwing Cloak<---at--->Fury of the Fallen

Queen's Gardens:
(36) Simple Key-City<---at--->Rancid Egg-Queen's Gardens
(60) Charm Notch-Grimm<---at--->Love Key
(66) Grimmchild<---at--->Queen's Gardens Stag
(118) Queen's Station Stag<---at--->Hallownest Seal-Queen's Gardens
(124) 380 Geo-Soul Master Chest<---at--->Queen Fragment

Royal Waterways:
(37) Pale Ore-Nosk<---at--->Flukenest
(38) Rancid Egg-Grubs<---at--->Mask Shard-Waterways
(39) Greenpath Stag<---at--->Rancid Egg-Waterways West Bluggsac
(45) Lumafly Lantern<---at--->Rancid Egg-Waterways Main
(70) Sprintmaster<---at--->Rancid Egg-Waterways East
(86) King's Idol-Dung Defender<---at--->King's Idol-Dung Defender
(95) Hallownest Seal-Queen's Gardens<---at--->Defender's Crest
(144) Howling Wraiths (1)<---at--->Rancid Egg-Waterways West Pickup

Ancient Basin:
(40) Isma's Tear<---at--->Wanderer's Journal-Ancient Basin
(42) Shade Soul<---at--->Simple Key-Basin
(71) Tram Pass<---at--->Pale Ore-Basin
(72) Hallownest Seal-Beast's Den<---at--->Monarch Wings
(76) Vessel Fragment-Sly2<---at--->Vessel Fragment-Basin

Resting Grounds:
(46) Charm Notch-Colosseum<---at--->150 Geo-Resting Grounds Chest
(48) World Sense<---at--->Resting Grounds Stag
(50) Arcane Egg-Lifeblood Core<---at--->Hallownest Seal-Resting Grounds Catacombs
(51) Mantis Claw<---at--->Dreamshield
(54) Hiveblood<---at--->Dream Nail
(81) Fragile Greed<---at--->Soul Eater
(98) Mask Shard-Crossroads Goam<---at--->Wanderer's Journal-Resting Grounds Catacombs
(106) Heavy Blow<---at--->Arcane Egg-Seer
(107) Charm Notch-Shrumal Ogres<---at--->Vessel Fragment-Seer
(108) Simple Key-Lurker<---at--->Pale Ore-Seer
(110) Simple Key-Sly<---at--->Dream Gate
(111) Mask Shard-Sly3<---at--->Hallownest Seal-Seer
(136) Vessel Fragment-Crossroads<---at--->Dream Wielder
(147) Weaversong<---at--->Awoken Dream Nail
(153) Monarch Wings<---at--->Mask Shard-Seer
(157) King's Idol-Grubs<---at--->Mask Shard-Grey Mourner

King's Station:
(47) Rancid Egg-Queen's Gardens<---at--->King's Station Stag
(52) Hidden Station Stag<---at--->Wanderer's Journal-King's Station
(55) Stag Nest Stag<---at--->Vessel Fragment-City
(168) Crystal Heart (1)<---at--->Hallownest Seal-King's Station

Kingdom's Edge:
(49) Hallownest Seal-Fog Canyon East<---at--->Wanderer's Journal-Kingdom's Edge Requires Dive
(69) Monomon<---at--->Rancid Egg-Upper Kingdom's Edge
(79) Hallownest Seal-King's Station<---at--->King's Idol-Pale Lurker
(80) Dreamshield<---at--->Rancid Egg-Near Quick Slash
(91) Pale Ore-Basin<---at--->Wanderer's Journal-Kingdom's Edge Entrance
(92) Wanderer's Journal-Above Mantis Village<---at--->Simple Key-Lurker
(93) Mask Shard-Hive<---at--->Dash Slash
(112) Wanderer's Journal-Fungal Wastes Thorns Gauntlet<---at--->Quick Slash
(130) King Fragment<---at--->King's Idol-Great Hopper
(166) King's Idol-Great Hopper<---at--->Wanderer's Journal-Kingdom's Edge Camp

Palace Grounds:
(53) Wanderer's Journal-Pleasure House<---at--->Hidden Station Stag
(173) Queen Fragment<---at--->King Fragment

Stag Nest:
(58) Cyclone Slash<---at--->Vessel Fragment-Stag Nest
(64) Mask Shard-Sly1<---at--->Stag Nest Stag

Stone Sanctuary:
(62) Great Slash<---at--->Mask Shard-Stone Sanctuary

Abyss:
(65) 655 Geo-Watcher Knights Chest<---at--->Abyss Shriek
(74) Glowing Womb<---at--->Shade Cloak
(89) Sharp Shadow<---at--->Arcane Egg-Shade Cloak
(150) Shaman Stone<---at--->Arcane Egg-Lifeblood Core
(156) Shade Cloak (1)<---at--->Lifeblood Core
(170) Hallownest Seal-Resting Grounds Catacombs<---at--->Arcane Egg-Birthplace
(171) Awoken Dream Nail<---at--->Void Heart

Soul Sanctum:
(68) Lifeblood Core<---at--->380 Geo-Soul Master Chest
(97) Mask Shard-5 Grubs<---at--->Desolate Dive
(99) Soul Eater<---at--->Spell Twister
(102) Mask Shard-Sly2<---at--->Hallownest Seal-Soul Sanctum

Beast's Den:
(78) Defender's Crest<---at--->Rancid Egg-Beast's Den
(96) Wanderer's Journal-King's Station<---at--->Hallownest Seal-Beast's Den
(137) Collector's Map<---at--->Herrah

Isma's Grove:
(83) Dash Slash<---at--->Isma's Tear

Crystallized Mound:
(84) Desolate Dive<---at--->Descending Dark

Deepnest:
(85) Nailmaster's Glory<---at--->Vessel Fragment-Deepnest
(100) Pale Ore-Grubs<---at--->Rancid Egg-Dark Deepnest
(104) Dream Nail<---at--->Hallownest Seal-Deepnest By Mantis Lords
(119) Shopkeeper's Key<---at--->Sharp Shadow
(122) Love Key<---at--->Pale Ore-Nosk
(146) Vessel Fragment-Seer<---at--->King's Idol-Deepnest
(164) Dream Nail (1)<---at--->Mask Shard-Deepnest

Overgrown Mound:
(87) Rancid Egg-Crystal Peak Tall Room<---at--->Howling Wraiths

Teacher's Archives:
(105) Hallownest Seal-Fungal Wastes Sporgs<---at--->Monomon

Spirit's Glade:
(109) 200 Geo-False Knight Chest<---at--->King's Idol-Glade of Hope

Weaver's Den:
(113) Simple Key-Basin<---at--->Weaversong
(117) Flukenest<---at--->160 Geo-Weavers Den Chest
(134) Monarch Wings (1)<---at--->Rancid Egg-Weaver's Den

Pleasure House:
(114) Isma's Tear (1)<---at--->Rancid Egg-City of Tears Pleasure House
(143) King's Station Stag<---at--->Wanderer's Journal-Pleasure House

Junk Pit:
(116) Vengeful Spirit (1)<---at--->Godtuner

(120) Sly (Key):
Rancid Egg-Near Quick Slash
Rancid Egg-Waterways East
Vessel Fragment-Stag Nest
Fragile Heart
Hallownest Seal-Grubs
85 Geo-Greenpath Chest
Hallownest Seal-Soul Sanctum

Tower of Love:
(127) Longnail<---at--->Collector's Map

Lake of Unn:
(129) Lifeblood Heart<---at--->Shape of Unn

Colosseum:
(140) City Crest<---at--->Pale Ore-Colosseum
(141) Hallownest Seal-Crossroads Well<---at--->Charm Notch-Colosseum

Blue Lake:
(151) Rancid Egg-Sly<---at--->Rancid Egg-Blue Lake

Distant Village:
(152) Baldur Shell<---at--->Distant Village Stag

Hallownest's Crown:
(158) Steady Body<---at--->Pale Ore-Crystal Peak

Hive:
(159) Mask Shard-Deepnest<---at--->Mask Shard-Hive
(163) Dream Wielder<---at--->Hiveblood

Black Egg Temple:
(161) Hallownest Seal-Seer<---at--->World Sense

Fungal Core:
(165) Void Heart (1)<---at--->Rancid Egg-Fungal Core

Cast Off Shell:
(174) Hallownest Seal-City Rafters<---at--->King's Brand

Failed Tramway:
(176) King's Idol-Cliffs<---at--->Tram Pass



SETTINGS
Seed: 732952683
Mode: Item Randomizer
Cursed: False
Start location: King's Pass
Random start items: False
REQUIRED SKIPS
Mild skips: False
Shade skips: False
Fireball skips: False
Acid skips: False
Spike tunnels: False
Dark Rooms: False
Spicy skips: False
RANDOMIZED LOCATIONS
Dreamers: True
Skills: True
Charms: True
Keys: True
Geo chests: True
Mask shards: True
Vessel fragments: True
Pale ore: True
Charm notches: True
Rancid eggs: True
Relics: True
Stags: True
Maps: False
Grubs: False
Whispering roots: False
Duplicate major items: True
QUALITY OF LIFE
Grubfather: True
Salubra: True
Early geo: True
Extra platforms: True
Levers: True
Jiji: False

Generated spoiler log in 0.0117113 seconds.`;
  },
};
</script>
