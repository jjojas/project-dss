<template>
  <v-app id="inspire">

    <v-app-bar app>
      <v-toolbar-title>Novel Recommendation System</v-toolbar-title>
    </v-app-bar>

    <v-main class="px-16">
     <v-autocomplete
            v-model="valuesNovel"
            :items="itemsNovel"
            outlined
            chips
            clearable
            deletable-chips
            multiple
            :loading="isLoadingNovel"
            :search-input.sync="searchNovel"
            return-object
            item-text="name"
            label="Judul Novel"
            hide-no-data
            hide-selected
            placeholder="Masukkan judul novel yang sudah pernah dibaca"
          ></v-autocomplete>
          <v-autocomplete
            v-model="valuesKategori"
            :items="itemsKategori"
            outlined
            chips
            clearable
            deletable-chips
            multiple
            :loading="isLoadingKategori"
            :search-input.sync="searchKategori"
            return-object
            label="Kategori"
            hide-no-data
            hide-selected
            placeholder="Masukkan kategori yang ingin difilter"
          ></v-autocomplete>
          <v-btn
          elevation="2"
          v-on:click="test"
          block
          color="primary"
          large
          >Rekomendasi</v-btn>

    <v-data-table
    :headers="headers"
    :items="recommend"
    :items-per-page="10"
  ></v-data-table>
  <v-overlay :value="isLoadingPage">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      headers: [
          { text: 'Judul', value: 'title' },
          { text: 'Penulis', value: 'author' },
        ],
      drawer: null,
      navitems: [
          { title: 'Recommend', icon: 'mdi-view-dashboard' },
          { title: 'About', icon: 'mdi-help-box' },
        ],
      // right: null,
      // items: [],
      valuesNovel: [],
      valuesKategori: [],
      value: null,
      descriptionLimit: 80,
      recommend: [],
      entriesNovel: [],
      entriesKategori: [],
      Novels: [],
      isLoadingNovel: false,
      isLoadingKategori: false,
      isLoadingPage: false,
      model: null,
      searchNovel: null,
      searchKategori: null,
    }),

    computed: {
      fields () {
        if (!this.model) return []

        return Object.keys(this.model).map(key => {
          return {
            key,
            value: this.model[key] || 'n/a',
          }
        })
      },
      itemsNovel () {
        return this.entriesNovel.map(entry => {
          const name = entry.name.length > this.descriptionLimit
            ? entry.name.slice(0, this.descriptionLimit) + '...'
            : entry.name

          return Object.assign({}, entry, { name })
        })
      },
      itemsKategori () {
        return this.entriesKategori.map(entry => {
          return entry
        })
      }
    },

    watch: {
      searchNovel (val) {
        // Items have already been loaded
        // if (this.items.length > 0) return

        // Items have already been requested
        if (this.isLoadingNovel) return

        this.isLoadingNovel = true

        // Lazily load input items
        // fetch('https://api.publicapis.org/entries')
        fetch('https://b00kr3com.herokuapp.com/book/'+val)
          .then(res => res.json())
          .then(res => {
            if (res.length > 0) {
              const ca = res.map(entry => {
                if (entry.hasOwnProperty('detail')) {
                  name = ""
                  return Object.assign({}, entry, { name });
                } else {
                  return entry;
                }
              }
              )
              if (this.itemsNovel.length > 0){
                this.entriesNovel = this.entriesNovel.concat(ca)
              } else {
                this.entriesNovel = ca
              }
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoadingNovel = false))
      },
      searchKategori (val) {
        // Items have already been loaded
        // if (this.items.length > 0) return

        // Items have already been requested
        if (this.isLoadingKategori) return

        this.isLoadingKategori = true

        // Lazily load input items
        // fetch('https://api.publicapis.org/entries')
        fetch('https://b00kr3com.herokuapp.com/tag/'+val)
          .then(res => res.json())
          .then(res => {
            if (res.length > 0) {
              const ca = res.map(entry => {
                if (entry.hasOwnProperty('detail')) {
                  name = ""
                  return Object.assign({}, entry, { name });
                } else {
                  return entry;
                }
              }
              )
              if (this.itemsKategori.length > 0){
                this.entriesKategori = this.entriesKategori.concat(ca)
              } else {
                this.entriesKategori = ca
              }
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoadingKategori = false))
      }
    },
    methods : {
      cetak: function (event){
          if (event){
            console.log(this.valuesNovel)
            console.log(this.valuesKategori)
          }
      },
      test: function(event){
        if(event){
          this.isLoadingPage = true
          this.Novels = this.valuesNovel.map(entry => {
              return entry.id;
            })
          }
          const rawResponse = fetch('https://b00kr3com.herokuapp.com/recommend/', {
                              method: 'POST',
                              headers: {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json'
                              },
                              body: JSON.stringify({tags: this.valuesKategori, books: this.Novels})
                              }).then(res => res.json())
                              .then(res => {
                                this.recommend = res
                              })
                              .catch(err => {
                                console.log(err)
                              }).finally(() => (this.isLoadingPage = false));
        }
      }
    }
</script>

<style scoped>
</style>