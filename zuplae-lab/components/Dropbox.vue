<template>
    <section>
        <b-field label="Fotos" expanded>
            <b-upload
                v-model="dropFiles"
                accept="image/*"
                multiple
                drag-drop
                expanded
            >
                <section class="section">
                    <div class="content has-text-centered">
                        <p>
                            <b-icon icon="upload" size="is-large"> </b-icon>
                        </p>
                        <p>Arraste as imagens aqui para enviá-las</p>
                    </div>
                </section>
            </b-upload>
        </b-field>

        <div class="tags">
            <span
                v-for="(file, index) in dropFiles"
                :key="index"
                class="tag is-primary"
            >
                {{ file.name }}
                <button
                    class="delete is-small"
                    type="button"
                    @click="deleteDropFile(index)"
                ></button>
            </span>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Dropbox',
    data() {
        return {
            dropFiles: []
        }
    },
    watch: {
        dropFiles() {
            this.emitEvent()
        }
    },
    methods: {
        deleteDropFile(index) {
            this.dropFiles.splice(index, 1)
        },
        emitEvent(event) {
            this.$emit('dropFilesChanged', this.dropFiles)
        }
    }
}
</script>
