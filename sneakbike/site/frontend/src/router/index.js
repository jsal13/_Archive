import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";

// Sneakops
import ResolutionStandards from "@/views/ResolutionStandards.vue";
import ReadmeGen from "@/views/ReadmeGen.vue";
import SBChecklist from "@/views/SBChecklist.vue";
import RaceDataTool from "@/views/RaceDataTool.vue";

// Sneakbike Setup & Sundry
import Setup from "@/views/Setup.vue";
import Schedule from "@/views/Schedule.vue";
import Team from "@/views/Team.vue";

// HKR Apps
import HKRDreamCatcher from "@/views/HKRDreamCatcher.vue";

// Bingo
import BingoALTTPR from '@/views/BingoALTTPR.vue'

// Testing Pages
import Test from '@/views/Test.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/schedule",
    name: "Schedule",
    component: Schedule,
  },
  {
    path: "/setup",
    name: "Setup",
    component: Setup,
  },

  {
    path: "/resolution-standards",
    name: "ResolutionStandards",
    component: ResolutionStandards,
  },
  {
    path: "/team",
    name: "Team",
    component: Team,
  },
  { path: "/readme-gen", name: "ReadmeGen", component: ReadmeGen },
  { path: "/checklist", name: "SBChecklist", component: SBChecklist },
  { path: "/race-data-tool", name: "RaceDataTool", component: RaceDataTool },
  { path: "/hkr/dream-catcher", name: "HKRDreamCatcher", component: HKRDreamCatcher },
  { path: "/bingo/alttp", name: "BingoALTTPR", component: BingoALTTPR },
  { path: "/test/test", name: "Test", component: Test }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
