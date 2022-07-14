<template>
    <Navigation />
</template>
<script>
import Navigation from './level1/Navigation.vue'
  export default {
    data() {
        return {
            mountains: []
        };
    },
    async fetch() {
    },
    components: { Navigation }
}
</script>