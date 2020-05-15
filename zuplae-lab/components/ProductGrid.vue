<template>
    <section class="section">
        <div class="columns is-3">
            <div
                v-for="product in products"
                :key="product.id"
                class="column is-one-quarter"
            >
                <Card
                    :price="product.price"
                    :price-was="product.promotionalPrice"
                    :title="product.name"
                    :thumbnail-photo-id="product.photos[0]"
                ></Card>
            </div>
        </div>
    </section>
</template>

<script>
import Card from '~/components/Card'
export default {
    name: 'ProductGrid',
    components: { Card },
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
