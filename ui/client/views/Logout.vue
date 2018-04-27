<template>

</template>

<script>
    export default {
        beforeMount: function() {
            this.$store.dispatch('logout')
            this.$router.push('/')
        }
    }
</script>