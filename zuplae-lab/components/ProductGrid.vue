<template>
    <section v-if="!loading" class="section">
        <div class="columns is-3">
            <div
                v-for="product in products"
                :key="product.id"
                class="column is-one-quarter"
            >
                <Card
                    :price="product.price"
                    :price-was="product.promotional_price"
                    :title="product.name"
                    :thumbnail-photo-id="product.photos[0]"
                ></Card>
            </div>
        </div>
    </section>
    <section v-else class="section">
        <div class="columns is-3">
            <div v-for="repeat in 4" :key="repeat" class="column is-one-fourth">
                <b-skeleton width="20%" :animated="true"></b-skeleton>
                <b-skeleton width="40%" :animated="true"></b-skeleton>
                <b-skeleton width="80%" :animated="true"></b-skeleton>
                <b-skeleton :animated="true"></b-skeleton>
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
        },
        loading: {
            type: Boolean,
            required: false,
            default() {
                return true
            }
        }
    }
}
</script>

<style scoped></style>
