<template>
  <div class="bg-white rounded-lg shadow-lg p-6">
    <div class="grid grid-cols-3 gap-4">
      <div class="col-span-1">
        <h3 class="text-gray-700 font-medium mb-2">Basic Info</h3>
        <div class="flex items-center space-x-2">
          <span class="text-gray-500">Gender:</span>
          <span class="text-gray-700">In-kwan</span>
        </div>
        <!-- Add other basic info fields -->
      </div>
      <div class="col-span-1">
        <h3 class="text-gray-700 font-medium mb-2">Sleep Time</h3>
        <div class="flex items-center space-x-2">
          <span class="text-gray-500">Dormitory:</span>
          <span class="text-gray-700">Ui-kwan</span>
        </div>
        <!-- Add other sleep time fields -->
      </div>
      <div class="col-span-1">
        <h3 class="text-gray-700 font-medium mb-2">Extra</h3>
        <div class="flex items-center space-x-2">
          <span class="text-gray-500">Smoking Stat.:</span>
          <span class="text-gray-700">Ye-kwan</span>
        </div>
        <!-- Add other extra fields -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserInfoCard'
};
</script>
