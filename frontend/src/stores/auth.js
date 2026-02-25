import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    user: JSON.parse(localStorage.getItem('user') || 'null')
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
    isAdmin: (state) => state.user?.role === 'admin'
  },
  actions: {
    async login(username, password) {
      try {
        const params = new URLSearchParams()
        params.append('username', username)
        params.append('password', password)
        
        const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'
        const response = await axios.post(`${baseUrl}/auth/token`, params)
        const { access_token } = response.data
        
        this.token = access_token
        
        // Simple decode for demo purposes
        const base64Url = access_token.split('.')[1]
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
        const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));
        
        const payload = JSON.parse(jsonPayload)
        this.user = { username: payload.sub, role: payload.role }
        
        localStorage.setItem('token', this.token)
        localStorage.setItem('user', JSON.stringify(this.user))
        
        return true
      } catch (error) {
        console.error('Login failed:', error)
        return false
      }
    },
    logout() {
      this.token = ''
      this.user = null
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      // Component should handle redirect
    }
  }
})
