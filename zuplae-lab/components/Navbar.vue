<template>
    <b-navbar class="is-dark">
        <template slot="brand">
            <b-navbar-item tag="nuxt-link" :to="{ path: '/' }">
                <h2>ZUPLAE</h2>
            </b-navbar-item>
        </template>

        <template v-if="!isLogged" slot="end">
            <b-navbar-item tag="nuxt-link" :to="{ path: '/dashboard' }">
                <div class="buttons">
                    <b-button icon-left="login" type="is-primary">
                        Entrar
                    </b-button>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
export default {
    name: 'Navbar',
    props: {
        isLogged: {
            type: Boolean,
            required: true
        }
    }
}
</script>

<style scoped></style>
