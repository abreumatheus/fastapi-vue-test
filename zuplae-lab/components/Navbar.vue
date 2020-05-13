<template>
    <b-navbar>
        <template slot="brand">
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <h2>ZUPLAE</h2>
            </b-navbar-item>
        </template>

        <template slot="end">
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button is-primary mdi mdi-login">
                        <strong>Enter</strong>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
export default {
    name: 'Navbar'
}
</script>

<style scoped></style>
