const admin = [
  {
    imgSrc: "cosmicordia.png",
    name: "cosmicordia",
    twitchUsername: "cosmicordia",
    jobs: "cofounder, production",
    descriptionText: '"It\'s in the cultural zeitgeist."',
  },
  {
    imgSrc: "jen_thehuman.png",
    name: "Jen_theHuman",
    twitchUsername: "Jen_theHuman",
    jobs: "social media lead, production",
    descriptionText: "Keeping things wholesome.",
  },
  {
    imgSrc: "melat0nin.png",
    name: "melat0nin",
    twitchUsername: "melat0nin",
    jobs: "cofounder, ops, frontend, production",
    descriptionText: '"...and I helped!"',
  },
]

const team = [
  {
    name: "Echo",
    imgSrc: "nijecho.jpg",
    twitchUsername: "nijecho",
    jobs: "artist",
    descriptionText: null,
  },
  {
    name: "ItsAceFace",
    imgSrc: "itsaceface.png",
    twitchUsername: "itsaceface",
    jobs: "production, moderator lead",
    descriptionText: null,
  },

  {
    imgSrc: "KiA00me.jpg",
    name: "KiA00me",
    twitchUsername: "KiA00me",
    jobs: "production, gamepicker lead",
    descriptionText: '"He scares me."',
  },
  {
    name: "Rascalnicough",
    imgSrc: "rascalnicough.png",
    twitchUsername: "Rascalnicough",
    jobs: "overlay design",
    descriptionText: null,
  },
  {
    name: "xchillhatterx",
    imgSrc: "xchillhatterx.jpg",
    twitchUsername: "xchillhatterx",
    jobs: "production",
    descriptionText: null,
  },
];


export default {
  namespaced: true,
  state: {
    admin: admin,
    team: team

  },

}