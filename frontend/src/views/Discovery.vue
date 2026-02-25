<template>
  <div class="discovery-page">
    <div class="flex justify-between items-center mb-8">
      <h1 class="text-3xl font-bold text-gray-800">Influencer Discovery</h1>
      <el-button type="primary" @click="dialogVisible = true">Add Influencer</el-button>
    </div>

    <div v-if="loading" class="flex justify-center py-10">
        <el-spinner />
    </div>
    
    <div v-else-if="influencers.length === 0" class="text-center py-10 text-gray-500">
        No influencers found. Add one to get started!
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <el-card v-for="influencer in influencers" :key="influencer.id" class="hover:shadow-lg transition-shadow">
            <template #header>
                <div class="flex items-center">
                    <el-avatar :size="50" :src="`https://ui-avatars.com/api/?name=${influencer.name}&background=random`" />
                    <div class="ml-4">
                        <h3 class="text-lg font-bold">{{ influencer.name }}</h3>
                        <p class="text-gray-500 text-sm">@{{ influencer.handle }} ({{ influencer.platform }})</p>
                    </div>
                </div>
            </template>
            <div class="text-center flex justify-between mb-4">
                <div>
                    <p class="text-xs text-gray-400 uppercase">Followers</p>
                    <p class="font-bold">{{ influencer.follower_count.toLocaleString() }}</p>
                </div>
                <div>
                    <p class="text-xs text-gray-400 uppercase">ER</p>
                    <p class="font-bold text-green-500">{{ influencer.engagement_rate }}%</p>
                </div>
            </div>
            <div class="mb-4">
                 <el-tag v-for="tag in (influencer.tags ? influencer.tags.split(',') : [])" :key="tag" class="mr-1 mb-1" size="small">{{ tag.trim() }}</el-tag>
            </div>
            <el-button class="w-full" type="primary" plain>Add to Campaign</el-button>
        </el-card>
    </div>

    <!-- Add Influencer Dialog -->
    <el-dialog v-model="dialogVisible" title="Add New Influencer" width="500px">
        <el-form :model="form" label-width="120px">
            <el-form-item label="Name">
                <el-input v-model="form.name" />
            </el-form-item>
            <el-form-item label="Handle">
                <el-input v-model="form.handle" />
            </el-form-item>
            <el-form-item label="Platform">
                <el-select v-model="form.platform" placeholder="Select platform">
                    <el-option label="Instagram" value="Instagram" />
                    <el-option label="TikTok" value="TikTok" />
                    <el-option label="YouTube" value="YouTube" />
                </el-select>
            </el-form-item>
            <el-form-item label="Category">
                <el-input v-model="form.category" />
            </el-form-item>
            <el-form-item label="Followers">
                <el-input-number v-model="form.follower_count" :min="0" />
            </el-form-item>
            <el-form-item label="Engagement Rate">
                <el-input-number v-model="form.engagement_rate" :min="0" :max="100" :precision="2" :step="0.1" />
            </el-form-item>
            <el-form-item label="Tags">
                <el-input v-model="form.tags" placeholder="Comma separated (e.g. fashion, tech)" />
            </el-form-item>
        </el-form>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="dialogVisible = false">Cancel</el-button>
                <el-button type="primary" @click="createInfluencer" :loading="submitting">Confirm</el-button>
            </span>
        </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import influencerApi from '../api/influencers'
import { ElMessage } from 'element-plus'

const influencers = ref([])
const loading = ref(true)
const dialogVisible = ref(false)
const submitting = ref(false)

const form = ref({
    name: '',
    handle: '',
    platform: '',
    category: '',
    follower_count: 0,
    engagement_rate: 0,
    tags: ''
})

const fetchInfluencers = async () => {
    loading.value = true
    try {
        const res = await influencerApi.getInfluencers()
        influencers.value = res.data
    } catch (error) {
        ElMessage.error('Failed to fetch influencers')
    } finally {
        loading.value = false
    }
}

const createInfluencer = async () => {
    submitting.value = true
    try {
        await influencerApi.createInfluencer(form.value)
        ElMessage.success('Influencer created successfully')
        dialogVisible.value = false
        // Reset form
        form.value = { name: '', handle: '', platform: '', category: '', follower_count: 0, engagement_rate: 0, tags: '' }
        // Refresh list
        fetchInfluencers()
    } catch (error) {
        ElMessage.error('Failed to create influencer')
    } finally {
        submitting.value = false
    }
}

onMounted(() => {
    fetchInfluencers()
})
</script>
