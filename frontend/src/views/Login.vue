<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <el-card class="w-96 shadow-lg rounded-xl">
      <div class="text-center mb-6">
        <h2 class="text-2xl font-bold text-gray-800">Welcome Back</h2>
        <p class="text-gray-500 text-sm">Sign in to KOL Connect</p>
      </div>
      <el-form :model="form" @submit.prevent="handleLogin">
        <el-form-item>
          <el-input v-model="form.username" placeholder="Username" :prefix-icon="User" />
        </el-form-item>
        <el-form-item>
          <el-input v-model="form.password" type="password" placeholder="Password" :prefix-icon="Lock" show-password />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit" class="w-full font-bold" :loading="loading">Sign In</el-button>
        </el-form-item>
      </el-form>
      <div class="text-center text-xs text-gray-400 mt-4">
        Default: admin / admin123
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { User, Lock } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()
const loading = ref(false)

const form = ref({
  username: '',
  password: ''
})

const handleLogin = async () => {
  if (!form.value.username || !form.value.password) {
    ElMessage.warning('Please enter username and password')
    return
  }
  
  loading.value = true
  const success = await authStore.login(form.value.username, form.value.password)
  loading.value = false
  
  if (success) {
    ElMessage.success('Login successful!')
    router.push('/')
  } else {
    ElMessage.error('Login failed. Please check credentials.')
  }
}
</script>
