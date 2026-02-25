import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import MainLayout from '../layout/MainLayout.vue'
import Dashboard from '../views/Dashboard.vue'
import Login from '../views/Login.vue'

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: { guest: true }
    },
    {
        path: '/',
        component: MainLayout,
        meta: { requiresAuth: true },
        children: [
            {
                path: '',
                name: 'Dashboard',
                component: Dashboard
            },
            {
                path: 'discovery',
                name: 'Discovery',
                component: () => import('../views/Discovery.vue')
            },
            {
                path: 'campaigns',
                name: 'Campaigns',
                component: () => import('../views/Campaigns.vue')
            },
            {
                path: 'samples',
                name: 'Samples',
                component: () => import('../views/Samples.vue'),
                meta: { requiresAdmin: true } // Example: Only admin can see samples
            }
        ]
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    const authStore = useAuthStore()
    
    if (to.meta.requiresAuth && !authStore.isAuthenticated) {
        next('/login')
    } else if (to.meta.guest && authStore.isAuthenticated) {
        next('/')
    } else if (to.meta.requiresAdmin && !authStore.isAdmin) {
        // Redirect to dashboard if not admin but tries to access admin route
        next('/')
    } else {
        next()
    }
})

export default router
