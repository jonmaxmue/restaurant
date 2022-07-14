<template>
     <b-navbar toggleable="lg" type="dark" variant="light">
    <b-navbar-brand href="#">
        <b-img src="~/assets/images/logo.png" />
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<script>
  export default {
    props: {
    },
    data() {
      return {
      }
    },
    mount(){

    },
  }
</script>

<style lang="sass" scoped>    
img
  height: 100px
</style>