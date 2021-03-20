import Vue from 'vue'
import { cloneDeep, get } from 'lodash';

const controllerSchemas = {
    'common': ['up', 'down', 'left', 'right'],
    'SNES': ['a', 'b', 'x', 'y', 'start', 'select', 'l', 'r'],
    'Genesis': ['a', 'b', 'c', 'x', 'y', 'z', 'start'],
    'NES': ['a', 'b', 'start', 'select']
}


export default {
    namespaced: true,
    state: {
        controllerData: {},
        consoles: {},
        hints: {},
        objectives: {}
    },
    mutations: {
        setControllerType(state, payload) {
            var valObj = Object.fromEntries(cloneDeep(controllerSchemas[payload.console].concat(controllerSchemas['common'])).map(x => [x, get(state.controllerData[payload.cardNum], x, '')]))
            Vue.set(state.controllerData, payload.cardNum, valObj)
            Vue.set(state.consoles, payload.cardNum, payload.console)
        },
        setControllerButton(state, payload) {
            Vue.set(state.controllerData[payload.cardNum], payload.button, payload.val)
        },

        setHint(state, payload) {
            Vue.set(state.hints, payload.cardNum, payload.val)
        },

        setObjective(state, payload) {
            Vue.set(state.objectives, payload.cardNum, payload.val)
        },

    },
    actions:
    {

    }

}