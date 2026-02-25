<template>
  <div class="samples-page">
    <div class="flex justify-between items-center mb-8">
      <h1 class="text-3xl font-bold text-gray-800">Sample Management</h1>
      <el-button type="primary">Ship New Sample</el-button>
    </div>

    <el-table :data="samples" style="width: 100%">
        <el-table-column prop="influencer" label="Influencer" width="180">
            <template #default="scope">
                <div class="flex items-center">
                    <el-avatar :size="24" :src="scope.row.avatar" />
                    <span class="ml-2">{{ scope.row.influencer }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="product" label="Product" width="180">
            <template #default="scope">
                <span class="font-medium text-gray-700">{{ scope.row.product }}</span>
            </template>
        </el-table-column>
        <el-table-column prop="tracking" label="Tracking ID" />
        <el-table-column prop="status" label="Status">
            <template #default="scope">
                <el-tag :type="scope.row.status === 'In Transit' ? 'warning' : 'success'">{{ scope.row.status }}</el-tag>
            </template>
        </el-table-column>
        <el-table-column label="Action">
            <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index, scope.row)">Track</el-button>
            </template>
        </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const samples = ref([
    {
        influencer: 'Sarah Jenkins',
        avatar: 'https://ui-avatars.com/api/?name=Sarah+J&background=random',
        product: 'Summer Dress',
        tracking: 'FDX-78239120',
        status: 'In Transit'
    },
    {
        influencer: 'Mike TechReview',
        avatar: 'https://ui-avatars.com/api/?name=Mike+T&background=random',
        product: 'Smart Watch X',
        tracking: 'UPS-12345678',
        status: 'Delivered'
    },
])

const handleEdit = (index, row) => {
    console.log(index, row)
}
</script>
