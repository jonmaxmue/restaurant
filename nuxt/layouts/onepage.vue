<template>
    <div>   
        <div id="header">
            <b-container>
                <Header />
            </b-container>
        </div>
        <Nuxt />
        <div id="footer" class="pt-7 pb-7">
            <b-container>
                <Footer />
            </b-container>
        </div>
    </div>
</template>

<style lang="sass">
#footer
    background-color: #152743
    color: $light


</style>