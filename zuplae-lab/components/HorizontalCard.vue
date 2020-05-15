<template>
    <div class="horizontal-card">
        <div class="box">
            <article class="media">
                <div class="media-left">
                    <figure class="is-1by1">
                        <img
                            :src="
                                'https://zuplae-tests.s3-sa-east-1.amazonaws.com/products/' +
                                    product.photos[0] +
                                    '.jpeg'
                            "
                            alt="Image"
                            width="155"
                            height="155"
                        />
                    </figure>
                </div>
                <div class="media-content">
                    <div class="content">
                        <h3>{{ product.name }}</h3>
                        <div
                            v-if="product.promotional_price"
                            class="if-promotional"
                        >
                            <small class="has-text-grey-light"
                                >de R$
                                {{ product.price.toFixed(2).replace('.', ',') }}
                                por</small
                            >
                            <br />
                            <strong
                                >R$
                                {{
                                    (product.promotional_price * 0.9)
                                        .toFixed(2)
                                        .replace('.', ',')
                                }}
                                à vista</strong
                            >
                            <br />
                            <small
                                >ou R$
                                {{
                                    product.promotional_price
                                        .toFixed(2)
                                        .replace('.', ',')
                                }}
                                em</small
                            >
                            <br />
                            <small
                                >10x de R$
                                {{
                                    (product.promotional_price / 10)
                                        .toFixed(2)
                                        .replace('.', ',')
                                }}
                                sem juros</small
                            >
                            <br />
                        </div>
                        <div v-else class="if-no-promo">
                            <strong
                                >R$
                                {{
                                    (product.price * 0.9)
                                        .toFixed(2)
                                        .replace('.', ',')
                                }}
                                à vista</strong
                            >
                            <br />
                            <small
                                >ou R$
                                {{ product.price.toFixed(2).replace('.', ',') }}
                                em</small
                            >
                            <br />
                            <small
                                >10x de R$
                                {{
                                    (product.price / 10)
                                        .toFixed(2)
                                        .replace('.', ',')
                                }}
                                sem juros</small
                            >
                            <br />
                        </div>
                    </div>
                    <nav class="level">
                        <div class="level-left">
                            <a
                                class="level-item"
                                aria-label="edit"
                                @click="isComponentModalActive = true"
                            >
                                <b-icon icon="pencil"> </b-icon>
                            </a>
                            <a
                                class="level-item"
                                aria-label="edit"
                                @click="$emit('deleteProduct', product)"
                            >
                                <b-icon icon="delete"> </b-icon>
                            </a>
                        </div>
                    </nav>
                </div>
            </article>
        </div>
        <b-modal
            :active.sync="isComponentModalActive"
            has-modal-card
            full-screen
            :can-cancel="false"
        >
            <edit-product
                :product="product"
                @refreshPage="$emit('refreshPage')"
            ></edit-product>
        </b-modal>
        <br />
    </div>
</template>

<script>
import EditProduct from '~/components/EditProduct'

export default {
    name: 'HorizontalCard',
    components: { EditProduct },
    props: {
        product: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            isComponentModalActive: false
        }
    }
}
</script>

<style scoped></style>
