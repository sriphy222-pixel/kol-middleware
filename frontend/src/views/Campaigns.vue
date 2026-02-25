<template>
  <div class="campaigns-page">
    <div class="flex justify-between items-center mb-8">
      <h1 class="text-3xl font-bold text-gray-800">Active Campaigns</h1>
      <el-button type="primary">Create New Campaign</el-button>
    </div>

    <el-card class="mb-6" v-for="campaign in campaigns" :key="campaign.id">
        <template #header>
            <div class="flex justify-between items-center">
                <h3 class="text-xl font-bold">{{ campaign.name }}</h3>
                <el-tag :type="campaign.status === 'Active' ? 'success' : 'info'">{{ campaign.status }}</el-tag>
            </div>
        </template>
        <div class="flex justify-between mb-4 text-gray-600">
            <div>
                <span class="block text-xs text-gray-400">Budget</span>
                <span class="font-medium">${{ campaign.budget }}</span>
            </div>
            <div>
                <span class="block text-xs text-gray-400">Influencers</span>
                <span class="font-medium">{{ campaign.influencersCount }}</span>
            </div>
            <div>
                <span class="block text-xs text-gray-400">ROI</span>
                <span class="font-medium text-green-500">{{ campaign.roi }}%</span>
            </div>
        </div>
        <el-progress :percentage="campaign.progress" :format="format" />
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const campaigns = ref([
    { id: 1, name: 'Summer Sale 2026', status: 'Active', budget: '15,000', influencersCount: 12, roi: 320, progress: 65 },
    { id: 2, name: 'New Gadget Launch', status: 'Active', budget: '25,000', influencersCount: 8, roi: 180, progress: 30 },
    { id: 3, name: 'Holiday Special', status: 'Draft', budget: '10,000', influencersCount: 0, roi: 0, progress: 0 },
])

const format = (percentage) => (percentage === 100 ? 'Full' : `${percentage}%`)
</script>
