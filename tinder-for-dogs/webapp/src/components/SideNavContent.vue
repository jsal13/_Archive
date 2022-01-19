<template>
    <v-navigation-drawer
        v-model="model"
        :mini-variant="miniVariant"
        :clipped="false"
        :floating="false"
        app
        overflow
    >
        <v-list>
            <v-list-item
                v-for="item in items"
                :key="item.title"
                link
                :to="item.path"
            >
            <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
            </v-list-item>
        </v-list>

        <template v-slot:append>
            <div class="pa-2">
                <v-btn block>Logout</v-btn>
            </div>
        </template>
    </v-navigation-drawer>
</template>

<script>
import { routes } from '../plugins/router';

export default {
    name: 'SideNavContent',
    props: {
        miniVariant: Boolean,
        model: String
    },
    data: () => ({
        apiAddress: process.env.VUE_APP_API_ADDRESS,
        items: routes.map(({ meta: { title, icon }, path }) => ({ title, path, icon }))
    })
}
</script>