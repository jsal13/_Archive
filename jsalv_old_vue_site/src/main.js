import Vue from 'vue';
import Vuex from 'vuex';
import readmeGenerator from '@/store/readmeGenerator';

import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

import 'prismjs';
// import 'prismjs/themes/prism.css';

require('@/styles/styles.css');

Vue.config.productionTip = false;

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: { readmeGenerator },
  strict: true,
});

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
