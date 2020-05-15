<template>
    <section id="dashboard">
        <section id="body" class="section">
            <div class="container">
                <h1 class="title is-1">Dashboard</h1>
                <div class="columns">
                    <SideMenu @componentChanged="switchComponentTab"></SideMenu>
                    <section class="column is-three-quarters">
                        <NewProduct
                            v-if="currentComponentTab === 'NewProduct'"
                        ></NewProduct>
                        <MyProducts
                            v-else-if="currentComponentTab === 'MyProducts'"
                            :products="products"
                        ></MyProducts>
                    </section>
                </div>
            </div>
        </section>
    </section>
</template>

<script>
import SideMenu from '~/components/SideMenu'
import NewProduct from '~/components/NewProduct'
import MyProducts from '~/components/MyProducts'

export default {
    name: 'Dashboard',
    components: { MyProducts, NewProduct, SideMenu },
    layout: 'Dashboard',
    data() {
        return {
            currentComponentTab: 'NewProduct',
            isProductsLoading: true,
            products: []
        }
    },
    watch: {
        currentComponentTab() {
            if (this.currentComponentTab === 'MyProducts') {
                this.getProdutcs()
            }
        }
    },
    methods: {
        switchComponentTab(value) {
            this.currentComponentTab = value
        },
        async getProdutcs() {
            this.products = await this.$axios.$get(
                'http://localhost:5000/api/products/'
            )
            this.isProductsLoading = false
        }
    },
    head() {
        return {
            title: 'Zuplae Dashboard'
        }
    }
}
</script>

<style scoped></style>
