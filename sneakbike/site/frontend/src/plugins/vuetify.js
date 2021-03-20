import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: false,
    themes: {
      light: {
        primary: colors.green.lighten2,
        secondary: colors.purple.lighten2,
        accent: colors.pink.lighten2,
        error: colors.red.lighten2,
        warning: colors.deepOrange.lighten4,
        info: colors.blue.lighten2,
        success: colors.teal.lighten2,
        anchor: colors.blue.lighten2,
      },
      dark: {
        primary: colors.teal.darken1,
        secondary: colors.purple.darken2,
        accent: colors.pink.darken2,
        error: colors.red.darken2,
        warning: colors.deepOrange.darken4,
        info: colors.blue.darken2,
        success: colors.teal.darken2,
        anchor: colors.blue.darken2,
      },
    },
  }
});
