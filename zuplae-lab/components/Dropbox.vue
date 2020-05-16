<template>
    <b-field class="file">
        <b-upload v-model="file" accept="image/*">
            <a class="button is-primary">
                <b-icon icon="upload"></b-icon>
                <span>Enviar Imagem</span>
            </a>
        </b-upload>
        <span v-if="file" class="file-name">
            {{ file.name }}
            <button
                class="delete is-small"
                type="button"
                @click="deleteFile()"
            ></button>
        </span>
    </b-field>
</template>

<script>
export default {
    name: 'Dropbox',
    props: {
        file: {
            type: Object,
            required: false,
            default() {
                return null
            }
        }
    },
    watch: {
        file() {
            this.emitEvent()
        }
    },
    methods: {
        deleteFile() {
            this.file = null
        },
        emitEvent(event) {
            this.$emit('dropFilesChanged', this.file)
        }
    }
}
</script>
