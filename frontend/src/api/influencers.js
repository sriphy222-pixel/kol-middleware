import axios from 'axios'

const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1',
    headers: {
        'Content-Type': 'application/json',
    },
})

export default {
    getInfluencers() {
        return apiClient.get('/influencers')
    },
    getInfluencer(id) {
        return apiClient.get(`/influencers/${id}`)
    },
    createInfluencer(data) {
        return apiClient.post('/influencers', data)
    },
}
