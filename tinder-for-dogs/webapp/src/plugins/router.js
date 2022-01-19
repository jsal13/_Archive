import Vue from 'vue';
import VueRouter from 'vue-router';

// Route components
import Home from '../Pages/Home';
import DogExplorer from '../Pages/DogExplorer';
import Favorites from '../Pages/Favorites';
import Friends from '../Pages/Friends';
import MatchedDogs from '../Pages/MatchedDogs';

Vue.use(VueRouter)

export const routes = [
    { path: '/', component: Home, meta: { title: "Home", icon: "fas fa-home" } },
    { path: '/dogs', component: DogExplorer, meta: { title: "Doggie DB", icon: "fas fa-search" } },
    { path: '/favorites', component: Favorites, meta: { title: "Favorites", icon: "fas fa-star" } },
    { path: '/friends', component: Friends, meta: { title: "Friends", icon: "fas fa-user-friends" } },
    { path: '/matches', component: MatchedDogs, meta: { title: "Matched", icon: "fas fa-heart" } },
]

export const router = new VueRouter({
    routes,
    mode: 'history'
})

