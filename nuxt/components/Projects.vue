<template>
    <div class="projects">
        <template v-for="project, index in projects" >
          <Level1Project :project="project" :revertOrder="index % 2 == 0" />
        </template>
    </div>
</template>

<script>
  export default {
    props: {
        projects: Array,
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
    
</style>