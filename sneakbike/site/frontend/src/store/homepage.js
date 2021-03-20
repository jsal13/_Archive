// If a pages value is a list: it's under a group (named the key).
// If a pages value is an object, it's a singleton under that name.
const pages = {
  "Resources": [
    { name: 'Setup', route: "/setup" },
    { name: 'Schedule', route: "/schedule" },
    { name: 'Sneakbike Team', route: '/team' }],
  "SneakOps Tools": [
    { name: "README Generator", route: "/readme-gen" },
    { name: "Race Day Checklist", route: "/checklist" },
    { name: "Race Data Tool", route: "/race-data-tool" },
    { name: "Resolution Standards", route: "/resolution-standards" }],
  "Rando Tools": [
    { name: "Hollow Knight QuickMode", route: "/hkr/dream-catcher" }],
  "Bingo": [
    { name: "ALTTPR Bingo", route: "/bingo/alttp" }]
}

const titleBarIcons = [
  { name: 'twitch', link: 'https://twitch.tv/sneakbike', icon: 'mdi-twitch' },
  { name: 'youtube', link: 'https://www.youtube.com/channel/UC5WLNGgGQH2tpNHM5uk2kCg', icon: 'mdi-youtube' },
  { link: 'https://www.github.com/jsal13/sneakbike/', icon: 'mdi-github' },
  { name: 'discord', link: '', icon: 'mdi-discord' }

]


export default {
  namespaced: true,
  state: {
    pages, titleBarIcons
  },
  mutations: {


  }
}