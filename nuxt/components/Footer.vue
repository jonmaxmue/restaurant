<template>
    <b-col class="footer">
        <b-row>
            <b-col cols="3">
                <img class="logo" src="~/assets/images/logo.png" />
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <ul>
                    <li>Restaurant RE GmbH</li>
                    <li>Straße zum Essen</li>
                    <li>01923 Freiland</li>
                </ul>
            </b-col>
            <b-col>
                <ul>
                    <li>Telefon 01922 121 432</li>
                    <li>E-Mail kontakt@restaurant.de</li>
                    <li>Web www.restaurant.de</li>
                </ul>
            </b-col>
            <b-col>
                <ul>
                    <li>Kontakt</li>
                    <li>Karriere</li>
                    <li>Services</li>
                </ul>
            </b-col>
            <b-col>
                <ul>
                    <li>FAQ</li>
                </ul>
            </b-col>
        </b-row>
    </b-col>
</template>

<script>
  export default {
    props: {
        projects: Object,
    },
    data() {
      return {
        mountains: []
      }
    },
    async fetch() {
      
    }
  }
</script>

<style lang="sass" scoped>
.footer
    ul
        list-style: none
        padding: 0

    img.logo
        width: 100%
        max-width: 200px
</style>