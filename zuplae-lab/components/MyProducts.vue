<template>
    <section class="container">
        <h1 class="title is-3">Meus Produtos</h1>
        <div v-if="!loading">
            <HorizontalCard
                v-for="product in products"
                :key="product.id"
                :product="product"
                @refreshPage="$emit('refreshPage')"
                @deleteProduct="deleteProduct(product)"
            ></HorizontalCard>
        </div>
        <template v-for="repeat in 4" v-else>
            <div :key="repeat">
                <b-skeleton width="20%" :animated="true"></b-skeleton>
                <b-skeleton width="40%" :animated="true"></b-skeleton>
                <b-skeleton width="80%" :animated="true"></b-skeleton>
                <b-skeleton :animated="true"></b-skeleton>
                <br />
            </div>
        </template>
    </section>
</template>

<script>
import HorizontalCard from '~/components/HorizontalCard'
export default {
    name: 'MyProducts',
    components: { HorizontalCard },
    props: {
        products: {
            type: Array[Object],
            required: true,
            default() {
                return []
            }
        },
        loading: {
            type: Boolean,
            required: false,
            default() {
                return true
            }
        }
    },
    computed: {
        getApiUrl() {
            return this.$store.state.baseApiURL
        }
    },
    methods: {
        deleteProduct(product) {
            this.$axios.$delete(this.getApiUrl + '/api/products/' + product.id)
            const index = this.products.indexOf(product)
            this.products.splice(index, 1)
            this.onSuccess('Produto deletado com sucesso!')
        },
        onSuccess(msg) {
            this.$buefy.toast.open({
                message: msg,
                type: 'is-success'
            })
            this.$emit('refreshPage')
        }
    }
}
</script>

<style scoped></style>
