<template>
    <section class="container">
        <h1 class="title is-3">Meus Produtos</h1>
        <HorizontalCard
            v-for="product in products"
            :key="product.id"
            :price="product.price"
            :price-was="product.priceWas"
            :title="product.name"
        ></HorizontalCard>
    </section>
</template>

<script>
import HorizontalCard from '~/components/HorizontalCard'
export default {
    name: 'MyProducts',
    components: { HorizontalCard },
    data() {
        return {
            products: {
                1: {
                    id: 1,
                    name: 'Notebook',
                    description: 'Um notebook',
                    price: 2500.0,
                    priceWas: 3600.0
                },
                2: {
                    id: 2,
                    name: 'iPhone',
                    description: 'Um celular',
                    price: 3600.0,
                    priceWas: 4500.0
                },
                3: {
                    id: 3,
                    name: 'PlayStation 4',
                    description: 'Um Videogame',
                    price: 2500.0,
                    priceWas: 3600.0
                },
                4: {
                    id: 4,
                    name: 'Smart TV',
                    description: 'Uma televisão smart',
                    price: 3600.0,
                    priceWas: 4500.0
                }
            }
        }
    }
}
</script>

<style scoped></style>
