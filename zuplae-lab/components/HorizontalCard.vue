<template>
    <div class="box">
        <article class="media">
            <div class="media-left">
                <figure class="is-1by1">
                    <img src="https://picsum.photos/155/155" alt="Image" />
                </figure>
            </div>
            <div class="media-content">
                <div class="content">
                    <h3>{{ title }}</h3>
                    <small v-if="priceWas" class="has-text-grey-light"
                        >de R$
                        {{ priceWas.toFixed(2).replace('.', ',') }}
                        por</small
                    >
                    <br />
                    <strong
                        >R$ {{ (price * 0.9).toFixed(2).replace('.', ',') }} à
                        vista</strong
                    >
                    <br />
                    <small
                        >ou R$
                        {{ price.toFixed(2).replace('.', ',') }} em</small
                    >
                    <br />
                    <small
                        >10x de R$
                        {{ (price / 10).toFixed(2).replace('.', ',') }} sem
                        juros</small
                    >
                </div>
                <nav class="level">
                    <div class="level-left">
                        <a class="level-item" aria-label="edit">
                            <b-icon icon="pencil"> </b-icon>
                        </a>
                        <a class="level-item" aria-label="edit">
                            <b-icon icon="delete"> </b-icon>
                        </a>
                    </div>
                </nav>
            </div>
        </article>
    </div>
</template>

<script>
export default {
    name: 'HorizontalCard',
    props: {
        title: {
            type: String,
            required: true
        },
        price: {
            type: Number,
            required: true
        },
        priceWas: {
            type: Number,
            required: false,
            default: null
        }
    }
}
</script>

<style scoped></style>
