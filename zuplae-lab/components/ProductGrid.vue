<template>
    <section class="section">
        <div class="columns is-3">
            <div class="column is-one-quarter">
                <Card :price="200.0" :price-was="250.0" title="Notebook"></Card>
            </div>
            <div class="column is-one-quarter">
                <Card :price="200.0" :price-was="250.0" title="Notebook"></Card>
            </div>
            <div class="column is-one-quarter">
                <Card :price="200.0" :price-was="250.0" title="Notebook"></Card>
            </div>
            <div class="column is-one-quarter">
                <Card :price="200.0" :price-was="250.0" title="Notebook"></Card>
            </div>
        </div>
    </section>
</template>

<script>
import Card from '~/components/Card'
export default {
    name: 'ProductGrid',
    components: { Card }
}
</script>

<style scoped></style>
