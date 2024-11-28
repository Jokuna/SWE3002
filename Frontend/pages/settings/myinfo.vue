<template>
  <div class="flex flex-col min-h-screen bg-gray-100">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Account Setting</h1>
    </div>

    <!-- Settings List -->
    <div class="flex-1 bg-white mt-4">
      <ul class="divide-y divide-gray-200">
        <li
          v-for="item in settings"
          :key="item.label"
          class="flex items-center justify-between px-6 py-4 hover:bg-gray-50 cursor-pointer"
        >
          <div class="flex items-center space-x-4">
            <span class="text-xl text-gray-600">{{ item.icon }}</span>
            <p class="text-gray-800 font-medium">{{ item.label }}</p>
          </div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 text-gray-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 5l7 7-7 7"
            />
          </svg>
        </li>
      </ul>
    </div>

    <!-- Bottom Navigation -->
    <div class="flex justify-around border-t bg-white py-4 mt-auto">
      <button class="text-gray-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
        <span class="text-xs mt-1">Search</span>
      </button>
      <button class="text-gray-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
        <span class="text-xs mt-1">Message</span>
      </button>
      <button class="text-blue-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-blue-500 rounded-full"></div>
        <span class="text-xs mt-1">Settings</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      settings: [
        { label: 'Gender', icon: '♂️♀️' },
        { label: 'Dormitory', icon: '🌬️' },
        { label: 'Smoking Status', icon: '✏️' },
        { label: 'Proportion', icon: '%' },
        { label: 'Sleep time', icon: '⏰' },
        { label: 'Age', icon: '⌛' },
        { label: 'Major', icon: '📊' },
        { label: 'Introduce my self', icon: '💬' },
        { label: 'Lastest GPA', icon: '📈' }
      ]
    };
  },
  head() {
    return {
      title: 'Account Setting - SKKU-Dormie'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
