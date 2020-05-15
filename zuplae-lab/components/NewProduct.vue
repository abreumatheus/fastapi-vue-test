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
                        v-model="category_id"
                        placeholder="Selecionar..."
                        expanded
                    >
                        <option :value="1">Eletrônicos</option>
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
            category_id: 1,
            description: '',
            price: 0,
            promotionalPrice: 0,
            photos: null
        }
    },
    methods: {
        submitProduct() {
            const requestBody = new FormData()
            requestBody.set('name', this.name)
            requestBody.set('category_id', this.category_id)
            requestBody.set('description', this.description)
            requestBody.set('price', this.price)
            requestBody.set('promotional_price', this.promotionalPrice)
            requestBody.append('photos', this.photos)
            this.$axios
                .$post('http://localhost:5000/api/products/', requestBody, {
                    headers: { 'Content-Type': 'multipart/form-data' }
                })
                .finally(() => this.successToast())
        },
        updatePhotos(value) {
            this.photos = value
        },
        successToast() {
            this.$buefy.toast.open({
                message: 'Produto cadastrado com sucesso!',
                type: 'is-success'
            })
            this.redirectToHome()
        },
        redirectToHome() {
            this.$router.push('/')
        }
    }
}
</script>

<style scoped></style>
