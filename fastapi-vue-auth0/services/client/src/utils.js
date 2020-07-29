import axios from 'axios'
import store from './store'
import { serviceAPIURL } from './config'

const USERS_ENDPOINT = `${serviceAPIURL}/users/self`

export const fetchCurrentUser = async (token) => {
  const { data } = await axios.get(USERS_ENDPOINT, {
    headers: {
      authorization: `Bearer ${token}`
    }
  })
  return data
}

export const createCurrentUser = async (user, token) => {
  const { data } = await axios.post(USERS_ENDPOINT, {
    username: user.nickname
  },
  {
    headers: {
      authorization: `Bearer ${token}`
    }
  })
  return data
}

export const onAuthenticationCallback = async (user, token) => {
  let data = {}
  try {
    data = await fetchCurrentUser(token)
  } catch (error) {
    if (error.response.status === 404) {
      data = await createCurrentUser(user, token)
    }
  }
  store.commit('updateProfile', data)
}
