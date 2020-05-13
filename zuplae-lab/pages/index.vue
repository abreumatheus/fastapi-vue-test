<template>
    <section id="index">
        <section id="cover" class="hero hero-home is-primary is-medium">
            <!-- Hero content: will be in the middle -->
            <div class="hero-body">
                <div class="columns is-centered is-vcentered">
                    <div class="column is-half has-text-centered">
                        <h1 class="title is-1">
                            ZUPLAE
                        </h1>
                        <h2 class="subtitle">
                            Your online store!
                        </h2>
                    </div>
                </div>
            </div>
        </section>

        <section id="body" class="section">
            <div class="container">
                <h1 class="title is-2">Products</h1>
                <ProductGrid></ProductGrid>
            </div>
        </section>
    </section>
</template>

<script>
import ProductGrid from '~/components/ProductGrid'
export default {
    name: 'Index',
    components: { ProductGrid },
    layout: 'Default',
    head() {
        return {
            title: 'Zuplae Store'
        }
    }
}
</script>

<style lang="scss" scoped>
@import '~bulma/sass/utilities/_all';
@import '~bulma/bulma';
@import '~buefy/src/scss/buefy';

.hero-home {
    @extend.hero;
    background-image: url('https://blog.rentcars.com/wp-content/uploads/2020/01/vila-germanica-blumenau-sc_2.jpg');
    background-position: bottom;
}
</style>
