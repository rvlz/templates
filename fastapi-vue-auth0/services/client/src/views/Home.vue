<template>
  <div>
    <h1>Home</h1>
    <p v-if="!$auth.loading && $auth.isAuthenticated">Welcome, {{ currentUser }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    currentUser () {
      return this.$store.state.profile.username
    }
  }
}
</script>
