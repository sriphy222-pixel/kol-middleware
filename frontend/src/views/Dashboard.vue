<template>
  <div class="dashboard-page">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <el-card class="bg-white rounded-xl shadow-sm border border-gray-100">
        <div class="flex items-center justify-between mb-4">
          <div class="bg-blue-100 p-3 rounded-lg text-blue-600">
            <el-icon><User /></el-icon>
          </div>
          <span class="text-xs font-semibold text-green-500 bg-green-50 px-2 py-1 rounded">+12%</span>
        </div>
        <h3 class="text-2xl font-bold text-gray-800">1,248</h3>
        <p class="text-sm text-gray-500">Total Influencers</p>
      </el-card>
      
      <el-card class="bg-white rounded-xl shadow-sm border border-gray-100">
        <div class="flex items-center justify-between mb-4">
          <div class="bg-purple-100 p-3 rounded-lg text-purple-600">
            <el-icon><DataLine /></el-icon>
          </div>
          <span class="text-xs font-semibold text-gray-500 bg-gray-50 px-2 py-1 rounded">Active</span>
        </div>
        <h3 class="text-2xl font-bold text-gray-800">8</h3>
        <p class="text-sm text-gray-500">Running Campaigns</p>
      </el-card>

      <el-card class="bg-white rounded-xl shadow-sm border border-gray-100">
        <div class="flex items-center justify-between mb-4">
          <div class="bg-yellow-100 p-3 rounded-lg text-yellow-600">
            <el-icon><Box /></el-icon>
          </div>
          <span class="text-xs font-semibold text-red-500 bg-red-50 px-2 py-1 rounded">Delayed: 2</span>
        </div>
        <h3 class="text-2xl font-bold text-gray-800">45</h3>
        <p class="text-sm text-gray-500">Samples In-Transit</p>
      </el-card>

      <el-card class="bg-white rounded-xl shadow-sm border border-gray-100">
        <div class="flex items-center justify-between mb-4">
          <div class="bg-green-100 p-3 rounded-lg text-green-600">
            <el-icon><Money /></el-icon>
          </div>
          <span class="text-xs font-semibold text-green-500 bg-green-50 px-2 py-1 rounded">+8.4%</span>
        </div>
        <h3 class="text-2xl font-bold text-gray-800">$42,500</h3>
        <p class="text-sm text-gray-500">Monthly GMV</p>
      </el-card>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
        <div class="flex justify-between items-center mb-4">
            <h3 class="font-bold text-gray-800">Recent Outreach Tasks</h3>
            <el-button text type="primary">View All</el-button>
        </div>
        <el-table :data="recentTasks" style="width: 100%">
            <el-table-column prop="influencer" label="Influencer" width="180">
                <template #default="scope">
                    <div class="flex items-center">
                        <el-avatar :size="24" :src="scope.row.avatar" />
                        <span class="ml-2">{{ scope.row.name }}</span>
                    </div>
                </template>
            </el-table-column>
            <el-table-column prop="platform" label="Platform" width="180">
                <template #default="scope">
                    <el-tag :type="scope.row.platform === 'TikTok' ? 'info' : (scope.row.platform === 'YouTube' ? 'danger' : 'warning')">{{ scope.row.platform }}</el-tag>
                </template>
            </el-table-column>
            <el-table-column prop="campaign" label="Campaign" />
            <el-table-column prop="status" label="Status">
                <template #default="scope">
                    <el-tag :type="scope.row.status === 'Pending Reply' ? 'warning' : 'success'">{{ scope.row.status }}</el-tag>
                </template>
            </el-table-column>
            <el-table-column prop="lastContact" label="Last Contact" />
        </el-table>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const recentTasks = ref([
    {
        name: 'Sarah Jenkins',
        avatar: 'https://ui-avatars.com/api/?name=Sarah+J&background=random',
        platform: 'TikTok',
        campaign: 'Summer Sale 2026',
        status: 'Pending Reply',
        lastContact: '2 hours ago'
    },
    {
        name: 'Mike TechReview',
        avatar: 'https://ui-avatars.com/api/?name=Mike+T&background=random',
        platform: 'YouTube',
        campaign: 'New Gadget Launch',
        status: 'Sample Sent',
        lastContact: 'Yesterday'
    },
    {
        name: 'Bella Rose',
        avatar: 'https://ui-avatars.com/api/?name=Bella+R&background=random',
        platform: 'Instagram',
        campaign: 'Fashion Week',
        status: 'Brief Sent',
        lastContact: '3 days ago'
    }
])
</script>
