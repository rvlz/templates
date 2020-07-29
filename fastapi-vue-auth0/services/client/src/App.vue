<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <span v-if="$auth.isAuthenticated">
        <router-link to="/profile">Profile</router-link> |
      </span>
      <span v-if="!$auth.loading">
        <a v-if="!$auth.isAuthenticated" @click.prevent="login">Log in</a>
        <a v-if="$auth.isAuthenticated" @click.prevent="logout">Log out</a>
      </span>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  methods: {
    login () {
      this.$auth.loginWithRedirect()
    },
    logout () {
      this.$auth.logout({
        returnTo: window.location.origin
      })
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;
    text-decoration: none;

    &:hover {
      cursor: pointer;
    }

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
