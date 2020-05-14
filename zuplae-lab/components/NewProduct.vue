<template>
    <section class="container">
        <h1 class="title is-3">Novo Produto</h1>
        <section>
            <b-field label="Nome">
                <b-input
                    v-model="name"
                    name="nome"
                    placeholder="Notebook Samsung"
                    expanded
                ></b-input>
            </b-field>

            <b-field grouped>
                <b-field label="Categoria" expanded>
                    <b-select
                        v-model="category"
                        placeholder="Selecionar..."
                        expanded
                    >
                        <option value="1">Bulma</option>
                        <option value="2">Vue.js</option>
                        <option value="3">Buefy</option>
                    </b-select>
                </b-field>
                <b-field label="Preço">
                    <vue-numeric
                        v-model="price"
                        class="input"
                        currency="R$"
                        :precision="2"
                        separator="."
                        placeholder="R$ 0,00"
                    ></vue-numeric>
                </b-field>
                <b-field label="Preço Promocional">
                    <vue-numeric
                        v-model="promotionalPrice"
                        class="input"
                        currency="R$"
                        :precision="2"
                        separator="."
                        placeholder="R$ 0,00"
                    ></vue-numeric>
                </b-field>
            </b-field>

            <b-field label="Descrição">
                <b-input v-model="description" type="textarea"></b-input>
            </b-field>

            <Dropbox @dropFilesChanged="updatePhotos"></Dropbox>

            <hr />

            <b-field>
                <b-button
                    type="is-primary"
                    icon-left="plus"
                    outlined
                    @click="submitProduct()"
                >
                    Criar
                </b-button>
            </b-field>
        </section>
    </section>
</template>

<script>
import VueNumeric from 'vue-numeric'
import Dropbox from '~/components/Dropbox'

export default {
    name: 'NewProduct',
    components: { Dropbox, VueNumeric },
    data() {
        return {
            name: '',
            category: '',
            description: '',
            price: 0,
            promotionalPrice: 0,
            photos: null
        }
    },
    methods: {
        submitProduct() {
            const response = {
                name: this.name,
                category: this.category,
                description: this.description,
                price: this.price,
                promotionalPrice: this.promotionalPrice,
                photos: this.photos
            }
            alert(JSON.stringify(response))
        },
        updatePhotos(value) {
            this.photos = value
        }
    }
}
</script>

<style scoped></style>
