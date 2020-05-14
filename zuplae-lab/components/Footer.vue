<template>
    <footer class="footer">
        <div class="content has-text-centered">
            <p><strong>Zuplae</strong> Copyright 2020</p>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style scoped lang="scss">
@import '~bulma/sass/utilities/_all';
@import '~bulma/bulma';
@import '~buefy/src/scss/buefy';
.footer {
    @extend.footer;
    position: relative;
    bottom: 0;
    width: 100%;
}
</style>
