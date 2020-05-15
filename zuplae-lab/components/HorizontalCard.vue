<template>
    <div class="box">
        <article class="media">
            <div class="media-left">
                <figure class="is-1by1">
                    <img
                        :src="
                            'https://zuplae-tests.s3-sa-east-1.amazonaws.com/products/' +
                                thumbnailPhotoId +
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
                    <h3>{{ title }}</h3>
                    <small v-if="promotionalPrice" class="has-text-grey-light"
                        >de R$
                        {{ promotionalPrice.toFixed(2).replace('.', ',') }}
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
        promotionalPrice: {
            type: Number,
            required: false,
            default: null
        },
        thumbnailPhotoId: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped></style>
