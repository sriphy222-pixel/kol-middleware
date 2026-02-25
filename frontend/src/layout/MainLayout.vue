<template>
  <div class="common-layout">
    <el-container class="min-h-screen">
      <!-- Mobile Overlay -->
      <div v-if="isMobileMenuOpen" class="fixed inset-0 bg-black bg-opacity-50 z-40 md:hidden" @click="isMobileMenuOpen = false"></div>
      
      <!-- Sidebar -->
      <el-aside 
        :width="isMobile ? '240px' : '200px'" 
        class="bg-slate-900 text-white min-h-screen fixed md:relative z-50 transition-transform duration-300 ease-in-out"
        :class="{ '-translate-x-full': isMobile && !isMobileMenuOpen, 'translate-x-0': !isMobile || isMobileMenuOpen }"
      >
        <div class="h-16 flex items-center justify-between px-4 border-b border-slate-700">
            <span class="text-xl font-bold tracking-wider text-purple-400">KOL<span class="text-white">CONNECT</span></span>
            <el-icon v-if="isMobile" class="text-white cursor-pointer" @click="isMobileMenuOpen = false"><Close /></el-icon>
        </div>
        <el-menu
            active-text-color="#ffd04b"
            background-color="#0f172a"
            class="el-menu-vertical-demo border-r-0"
            :default-active="$route.path"
            text-color="#fff"
            router
            @select="handleMenuSelect"
        >
            <el-menu-item index="/">
                <el-icon><Menu /></el-icon>
                <span>Dashboard</span>
            </el-menu-item>
            <el-menu-item index="/discovery">
                <el-icon><Search /></el-icon>
                <span>Discovery</span>
            </el-menu-item>
            <el-menu-item index="/campaigns">
                <el-icon><DataLine /></el-icon>
                <span>Campaigns</span>
            </el-menu-item>
            <el-menu-item v-if="authStore.isAdmin" index="/samples">
                <el-icon><Box /></el-icon>
                <span>Samples</span>
            </el-menu-item>
        </el-menu>
      </el-aside>

      <el-container class="transition-all duration-300">
        <el-header class="bg-white border-b border-gray-200 flex items-center justify-between px-4 h-16 sticky top-0 z-30">
            <div class="flex items-center">
                <el-icon v-if="isMobile" class="mr-4 text-gray-600 text-xl cursor-pointer" @click="isMobileMenuOpen = true"><Expand /></el-icon>
                <h2 class="text-lg md:text-xl font-semibold text-gray-800 truncate">{{ $route.name }}</h2>
            </div>
            <div class="flex items-center">
                <el-dropdown trigger="click">
                    <div class="flex items-center cursor-pointer">
                        <el-avatar :size="32" :src="`https://ui-avatars.com/api/?name=${authStore.user?.username || 'User'}&background=random`" />
                        <span class="hidden md:inline ml-2 text-sm text-gray-600">{{ authStore.user?.username || 'User' }}</span>
                        <el-icon class="hidden md:inline el-icon--right"><arrow-down /></el-icon>
                    </div>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item class="md:hidden" disabled>{{ authStore.user?.username }} ({{ authStore.user?.role }})</el-dropdown-item>
                            <el-dropdown-item divided class="md:hidden"></el-dropdown-item>
                            <el-dropdown-item @click="handleLogout">Logout</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </div>
        </el-header>
        <el-main class="bg-gray-50 p-4 md:p-6 overflow-x-hidden">
            <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'
import { ArrowDown, Expand, Close, Menu, Search, DataLine, Box } from '@element-plus/icons-vue'

const authStore = useAuthStore()
const router = useRouter()
const isMobileMenuOpen = ref(false)
const windowWidth = ref(window.innerWidth)

const isMobile = computed(() => windowWidth.value < 768)

const handleResize = () => {
    windowWidth.value = window.innerWidth
    if (!isMobile.value) {
        isMobileMenuOpen.value = false
    }
}

const handleMenuSelect = () => {
    if (isMobile.value) {
        isMobileMenuOpen.value = false
    }
}

const handleLogout = () => {
    authStore.logout()
    router.push('/login')
}

onMounted(() => {
    window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
    window.removeEventListener('resize', handleResize)
})
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  min-height: 400px;
}
</style>
