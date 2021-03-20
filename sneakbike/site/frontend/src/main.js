import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import VueAnalytics from "vue-router";
import router from "./router";

//Vuex Stores
import Vuex from 'vuex'
import readmeGeneratorStore from '@/store/readmeGenerator.js'
import hkrStore from '@/store/hkr.js'
import homepage from '@/store/homepage.js'
import team from '@/store/team.js'
import checklist from '@/store/checklist.js'

import VueLodash from "vue-lodash";
import lodash from "lodash";

// Prism -- Highlighting Syntax.
import "prismjs";
import "prismjs/themes/prism-tomorrow.css";
import "prismjs/components/prism-powershell.min";
import "prismjs/components/prism-markup.min";
import "prismjs/plugins/autolinker/prism-autolinker.min";
import "prismjs/plugins/autolinker/prism-autolinker.css";
import Prism from "vue-prism-component";

// Common Cards
import InfoCard from "@/components/Common/InfoCard.vue";
import WarningCard from "@/components/Common/WarningCard.vue";

//Styles
import './styles/style.scss'

Vue.config.productionTip = false;

Vue.component("prism", Prism);
Vue.component("info-card", InfoCard);
Vue.component("warning-card", WarningCard);
Vue.use(VueLodash, { lodash: lodash });

Vue.use(Vuex)
Vue.use(VueAnalytics, {
  appName: "Sneakbike Website",
  appVersion: "1.0",
  trackingId: "UA-180310014-1",
  vueRouter: router,
});

const store = new Vuex.Store({
  modules: { 'hkr': hkrStore, 'readmeGenerator': readmeGeneratorStore, 'homepage': homepage, 'team': team, 'checklist': checklist },
  strict: true
})

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
