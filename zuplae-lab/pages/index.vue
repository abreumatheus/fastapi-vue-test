<template>
    <section id="index">
        <section id="cover" class="hero hero-home is-primary is-medium">
            <!-- Hero content: will be in the middle -->
            <div class="hero-body">
                <div class="columns is-centered is-vcentered">
                    <div class="column is-half has-text-centered">
                        <h1 id="main-title" class="title is-1">
                            <br />
                        </h1>
                        <h2 class="subtitle"><br /></h2>
                    </div>
                </div>
            </div>
        </section>

        <section id="body" class="section">
            <div class="container">
                <h1 class="title is-2">Produtos</h1>
                <ProductGrid
                    v-if="!isProductsGridLoading"
                    :products="products"
                ></ProductGrid>
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
    data() {
        return {
            products: [],
            isProductsGridLoading: true
        }
    },
    mounted() {
        return this.getProdutcs()
    },
    methods: {
        async getProdutcs() {
            this.products = await this.$axios.$get(
                'http://localhost:5000/api/products/'
            )
            this.isProductsGridLoading = false
        }
    },
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
    background-image: url('https://s.mlcdn.com.br/banner/campanhas/1305deskgalaxyflip.png');
    background-position: center;
    background-repeat: no-repeat;
}
#main-title {
    color: #8c67ef;
}
</style>
