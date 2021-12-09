import Vue from 'vue'
import VueRouter from 'vue-router'
import Overview from '../views/Overview.vue'
import Match from '../views/Match.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Overview',
        component: Overview
    },
    {
        path: '/match/:teamA/:teamH',
        component: Match,
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router

