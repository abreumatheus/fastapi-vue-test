<template>
    <div class="modal-card" style="width: auto">
        <header class="modal-card-head">
            <p class="modal-card-title">Editar Produto</p>
        </header>
        <section class="modal-card-body">
            <b-field label="Nome">
                <b-input
                    v-model="product.name"
                    name="nome"
                    placeholder="Notebook Samsung"
                    expanded
                ></b-input>
            </b-field>

            <b-field grouped>
                <b-field label="Categoria" expanded>
                    <b-select
                        v-model="product.category_id"
                        placeholder="Selecionar..."
                        expanded
                    >
                        <option :value="1">Eletrônicos</option>
                    </b-select>
                </b-field>
                <b-field label="Preço">
                    <vue-numeric
                        v-model="product.price"
                        class="input"
                        currency="R$"
                        :precision="2"
                        separator="."
                    ></vue-numeric>
                </b-field>
                <b-field label="Preço Promocional">
                    <vue-numeric
                        v-model="product.promotional_price"
                        class="input"
                        currency="R$"
                        :precision="2"
                        separator="."
                    ></vue-numeric>
                </b-field>
            </b-field>

            <b-field label="Descrição">
                <b-input
                    v-model="product.description"
                    type="textarea"
                ></b-input>
            </b-field>
            <hr />
        </section>
        <footer class="modal-card-foot">
            <b-field>
                <b-button type="is-danger" outlined @click="$parent.close()">
                    Cancelar
                </b-button>

                <b-button
                    type="is-primary"
                    icon-left="plus"
                    outlined
                    @click="submitProduct()"
                >
                    Atualizar
                </b-button>
            </b-field>
        </footer>
    </div>
</template>

<script>
import VueNumeric from 'vue-numeric'

export default {
    name: 'EditProduct',
    components: { VueNumeric },
    props: {
        product: {
            type: Object,
            required: true
        }
    },
    computed: {
        getApiUrl() {
            return this.$store.state.baseApiURL
        }
    },
    methods: {
        submitProduct() {
            const requestBody = new FormData()
            requestBody.set('name', this.product.name)
            requestBody.set('category_id', this.product.category_id)
            requestBody.set('description', this.product.description)
            requestBody.set('price', this.product.price)
            requestBody.set('promotional_price', this.product.promotional_price)
            this.$axios
                .$put(
                    this.getApiUrl + '/api/products/' + this.product.id,
                    requestBody,
                    {
                        headers: { 'Content-Type': 'multipart/form-data' }
                    }
                )
                .finally(() =>
                    this.onSuccess('Produto cadastrado com sucesso!')
                )
        },
        onSuccess(msg) {
            this.$buefy.toast.open({
                message: msg,
                type: 'is-success'
            })
            this.$parent.close()
            this.$emit('refreshPage')
        }
    }
}
</script>

<style scoped></style>
