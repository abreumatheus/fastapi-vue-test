<template>
    <section class="container">
        <h1 class="title is-3">Meus Produtos</h1>
        <HorizontalCard
            v-for="product in products"
            :key="product.id"
            :price="product.price"
            :promotional-price="product.promotionalPrice"
            :title="product.name"
            :thumbnail-photo-id="product.photos[0]"
        ></HorizontalCard>
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
        }
    }
}
</script>

<style scoped></style>
