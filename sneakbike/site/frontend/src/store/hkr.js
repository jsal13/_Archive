import Vue from 'vue'
import { cloneDeep } from 'lodash';

const locData = {
    Abyss: {
        background: "#707170",
        border: "#242524",
        abbr: "Abyss",
        displayName: 'Abyss',
        show: true,
        items: []
    },
    Ancient_Basin: {
        background: "#73747d",
        border: "#282a37",
        abbr: "AnBsn",
        displayName: 'Ancient Basin',
        show: true,
        items: []
    },
    City_of_Tears: {
        background: "#6b89a9",
        border: "#1b4a7b",
        abbr: "CityT",
        displayName: 'City of Tears',
        show: true,
        items: []
    },
    Crystal_Peak: {
        background: "#b588b0",
        border: "#95568f",
        abbr: "CryPk",
        displayName: 'Crystal Peak',
        show: true,
        items: []
    },
    Deepnest: {
        background: "#666b80",
        border: "#141c3c",
        abbr: "DNest",
        displayName: 'Deepnest',
        show: true,
        items: []
    },
    Dirtmouth: {
        background: "#787994",
        border: "#2f315b",
        abbr: "Dirtm",
        displayName: 'Dirtmouth',
        show: true,
        items: []
    },
    Fog_Canyon: {
        background: "#9da3bd",
        border: "#5b6591",
        abbr: "FogCn",
        displayName: 'Fog Canyon',
        show: true,
        items: []
    },
    Forgotten_Crossroads: {
        background: "#687796",
        border: "#202d5d",
        abbr: "FxRds",
        displayName: 'Forgotten Crossroads',
        show: true,
        items: []
    },
    Fungal_Wastes: {
        background: "#58747c",
        border: "#113945",
        abbr: "FungW",
        displayName: 'Fungal Wastes',
        show: true,
        items: []
    },
    Greenpath: {
        background: "#679487",
        border: "#155b47",
        abbr: "GPath",
        displayName: 'Greenpath',
        show: true,
        items: []
    },
    Hive: {
        background: "#C17F6E",
        border: "#A64830",
        abbr: "Hive",
        displayName: 'Hive',
        show: true,
        items: []
    },
    Howling_Cliffs: {
        background: "#75809a",
        border: "#3b4a6f",
        abbr: "HClif",
        displayName: 'Howling Cliffs',
        show: true,
        items: []
    },
    Kingdoms_Edge: {
        background: "#768384",
        border: "#3c4e50",
        abbr: "KEdge",
        displayName: 'Kingdom\'s Edge',
        show: true,
        items: []
    },
    Queens_Gardens: {
        background: "#559f9d",
        border: "#0d7673",
        abbr: "QGdn",
        displayName: 'Queen\'s Garden',
        show: true,
        items: []
    },
    Resting_Grounds: {
        background: "#84799d",
        border: "#423169",
        abbr: "RestG",
        displayName: 'Resting Grounds',
        show: true,
        items: []
    },
    Royal_Waterways: {
        background: "#6d919d",
        border: "#1e5669",
        abbr: "RWatr",
        displayName: 'Royal Waterways',
        show: true,
        items: []
    },
}

export default {
    namespaced: true,
    state: {
        itemFoundState: { type: Object },
        showDreamers: true,
        showAbilities: true,
        showUsefulItems: false,
        timerValue: 0,
        arrayDreamers: [],
        arrayAbilities: [],
        arrayUsefulItems: [],
        arrayLocDataObj: []
    },
    mutations: {
        setArrayDreamers(state, payload) {
            state.arrayDreamers = payload.value
        },
        setArrayAbilities(state, payload) {
            state.arrayAbilities = payload.value
        },
        setArrayUsefulItems(state, payload) {
            state.arrayUsefulItems = payload.value
        },
        setTimerValue(state, payload) {
            state.timerValue = payload.val
        },
        setItemFoundState(state, payload) {
            Vue.set(state.itemFoundState, payload.name, payload.value)
        },
        toggleDreamers(state) {
            state.showDreamers = !state.showDreamers
        },
        toggleAbilities(state) {
            state.showAbilities = !state.showAbilities
        },
        toggleUsefulItems(state) {
            state.showUsefulItems = !state.showUsefulItems
        },
        defineLocObject(state) {
            // This adds items to the locData above.}
            var arraysToConcat = [];
            if (state.showDreamers) {
                arraysToConcat.push(state.arrayDreamers);
            }
            if (state.showAbilities) {
                arraysToConcat.push(state.arrayAbilities);
            }
            if (state.showUsefulItems) {
                arraysToConcat.push(state.arrayUsefulItems);
            }

            if (Object.keys(state.arrayDreamers).length === 0) { return; } // If the user hasn't uploaded the file yet.

            const unorderedData = [].concat(...arraysToConcat).reduce((result, item) => {
                const specificLocData = { ...cloneDeep(locData[item[0]]), ...result[item[0]] }
                specificLocData['items'].push(item[1])
                specificLocData['items'].sort()

                result[item[0]] = { ...result[item[0]], ...specificLocData };

                return result
            }, {});

            const orderedData = Object.fromEntries(Object.entries(unorderedData).sort());

            state.arrayLocDataObj = orderedData;
        },
        toggleLocationInLocDataObj(state, payload) {
            // payload = {'loc': str }
            Vue.set(state.arrayLocDataObj[payload.loc], 'show', !state.arrayLocDataObj[payload.loc]['show'])

        }
    },
    actions:
    {
        toggleDreamersAndRefresh: ({ commit }) => {
            commit('toggleDreamers')
            commit('defineLocObject')
        },

        toggleAbilitiesAndRefresh: ({ commit }) => {
            commit('toggleAbilities')
            commit('defineLocObject')
        },

        toggleUsefulItemsAndRefresh: ({ commit }) => {
            commit('toggleUsefulItems')
            commit('defineLocObject')
        },
    }

}