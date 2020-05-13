<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by5">
                <img
                    src="https://picsum.photos/864/1080"
                    alt="Placeholder image"
                />
            </figure>
        </div>
        <div class="card-content">
            <div class="media">
                <div class="media-content">
                    <p class="title is-4">{{ title }}</p>
                </div>
            </div>

            <div class="content">
                <small v-if="priceWas" class="has-text-grey-light"
                    >de R$ {{ priceWas }} por</small
                >
                <br />
                <strong>R$ {{ price * 0.9 }} à vista</strong>
                <br />
                <small>ou R$ {{ price }} em</small>
                <br />
                <small>10x de R$ {{ price / 10 }} sem juros</small>
            </div>
            <div class="card-footer">
                <b-button type="is-primary" expanded>Ver</b-button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Card',
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
