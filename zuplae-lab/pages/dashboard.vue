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
                            @refreshPage="goToHome"
                        ></NewProduct>
                        <MyProducts
                            v-else-if="currentComponentTab === 'MyProducts'"
                            :products="products"
                            :loading="isProductsLoading"
                            @refreshPage="refreshPage"
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
    computed: {
        getApiUrl() {
            return this.$store.state.baseApiURL
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
            this.isProductsLoading = true
            this.products = []
            this.products = await this.$axios.$get(
                this.getApiUrl + '/api/products/'
            )
            this.isProductsLoading = false
        },
        goToHome() {
            this.$router.push('/')
        },
        refreshPage() {
            this.$router.go()
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
