import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Auth0Plugin } from './auth'
import { onAuthenticationCallback } from './utils'
import { domain, clientId, audience } from './config'

Vue.use(Auth0Plugin, {
  domain,
  clientId,
  audience,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    )
  },
  onAuthenticationCallback
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
