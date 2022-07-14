<template>
    <b-row>
        <b-col class="col-6 d-flex align-items-center justify-content-center" :class="{'order-1': !revertOrder }">
          <div>
            <h2>{{ project.title }}</h2>
            <p>{{ project.description }}</p>
          </div>
        </b-col>
        <b-col class="col-6">
          <img :src="project.image" />
        </b-col>
    </b-row>
</template>
<script>
  export default {
    props: {
        project: Object,
        revertOrder: Boolean
    },
    data() {
      return {
        mountains: [],
      }
    },
    mount(){

    },
  }
</script>

<style lang="sass" scoped>    
    img
      width: 100%
      object-fit: cover
    
    p
      max-width: 500px
</style>