<template>
  <div>
    <div>
      <img :src="$auth.user.picture">
      <h2>{{ $auth.user.name }}</h2>
      <p>{{ $auth.user.email }}</p>
    </div>
    <button @click="getToken">click</button>
    <div>
      <pre>{{ JSON.stringify($auth.user, null, 2) }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  methods: {
    async getToken () {
      console.log(await this.$auth.getTokenSilently())
    }
  }
}
</script>
