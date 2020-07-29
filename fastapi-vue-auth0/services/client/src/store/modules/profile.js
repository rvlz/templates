
export const moduleProfile = {
  state: () => ({}),
  mutations: {
    updateProfile (state, data) {
      state.email = data.email
      state.username = data.username
      state.is_active = data.is_active
    }
  }
}
