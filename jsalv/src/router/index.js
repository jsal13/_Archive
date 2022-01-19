import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '@/views/Home.vue';
import Apps from '@/views/Apps.vue';
import ReadmeGen from '@/views/ReadmeGen.vue';
import SBRaceDataTool from '@/views/SBRaceDataTool.vue';
import GamepickerGameInfo from '@/views/GamepickerGameInfo.vue';
import LicensePlatePractice from '@/views/LicensePlatePractice.vue';
import TopicGenerator from '@/views/TopicGenerator.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/app',
    name: 'Apps',
    component: Apps,
  },
  {
    path: '/app/readme-gen',
    name: 'ReadmeGen',
    component: ReadmeGen,
  },
  {
    path: '/app/race-data-tool',
    name: 'SBRaceDataTool',
    component: SBRaceDataTool,
  },
  {
    path: '/app/gamepicker-game-info',
    name: 'GamepickerGameInfo',
    component: GamepickerGameInfo,
  },
  {
    path: '/app/license-plate-practice',
    name: 'LicensePlatePractice',
    component: LicensePlatePractice,
  },
  {
    path: '/app/topic-generator',
    name: 'TopicGenerator',
    component: TopicGenerator,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
