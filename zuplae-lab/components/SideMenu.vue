<template>
    <b-menu class="column is-one-quarter">
        <b-menu-list label="Menu">
            <b-menu-item
                icon="plus"
                label="Novo Produto"
                active
                @click="activeComponent = 'NewProduct'"
            ></b-menu-item>
        </b-menu-list>
        <b-menu-list label="Meus Produtos">
            <b-menu-item
                label="Todos"
                @click="activeComponent = 'MyProducts'"
            ></b-menu-item>
        </b-menu-list>
        <b-menu-list label="Ações">
            <b-menu-item
                tag="nuxt-link"
                :to="{ path: '/' }"
                label="Logout"
            ></b-menu-item>
        </b-menu-list>
    </b-menu>
</template>

<script>
export default {
    name: 'SideMenu',
    data() {
        return {
            activeComponent: 'NewProduct'
        }
    },
    watch: {
        activeComponent() {
            this.emitComponentChange()
        }
    },
    methods: {
        emitComponentChange(event) {
            this.$emit('componentChanged', this.activeComponent)
        }
    }
}
</script>
