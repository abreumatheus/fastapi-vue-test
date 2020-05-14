<template>
    <section id="nav" class="page-wrapper">
        <Navbar :is-logged="true"></Navbar>
        <Nuxt class="content-wrapper" />
        <Footer></Footer>
    </section>
</template>

<script>
import Navbar from '~/components/Navbar'
import Footer from '~/components/Footer'
export default {
    name: 'Dashboard',
    components: { Footer, Navbar }
}
</script>

<style scoped>
.page-wrapper {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
}

.content-wrapper {
    flex: 1;
}
</style>
