<template>
  <div
    class="flex flex-col items-center justify-center min-h-screen bg-gray-100"
  >
    <div class="w-full max-w-md bg-white rounded-lg shadow-md">
      <!-- Tabs Navigation -->
      <div class="flex border-b">
        <button
          class="flex-1 py-2 text-blue-500 border-b-2 border-blue-500 font-medium"
        >
          Basic Info
        </button>
        <button
          class="flex-1 py-2 text-gray-500 border-b-2 border-transparent hover:text-blue-500"
        >
          Sleep Time
        </button>
        <button
          class="flex-1 py-2 text-gray-500 border-b-2 border-transparent hover:text-blue-500"
        >
          Extra
        </button>
      </div>

      <!-- Matching List -->
      <div class="divide-y divide-gray-200">
        <div
          v-for="(item, index) in matchingList"
          :key="index"
          class="flex items-center justify-between px-4 py-3 hover:bg-gray-50"
        >
          <div class="flex items-center space-x-3">
            <div
              class="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center"
            >
              <img
                v-if="item.image"
                :src="item.image"
                alt="profile"
                class="w-full h-full rounded-full"
              />
            </div>
            <div>
              <p class="font-medium text-gray-800">{{ item.name }}</p>
              <p class="text-sm text-gray-500">
                Matching Rate : {{ item.matchRate }}%
              </p>
            </div>
          </div>
          <button class="text-gray-400 hover:text-gray-600">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
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
          </button>
        </div>
      </div>

      <!-- Bottom Navigation -->
      <div class="flex justify-around border-t mt-6 pt-4 bg-white">
        <button class="text-blue-500 flex flex-col items-center">
          <div class="w-6 h-6 bg-blue-500 rounded-full"></div>
          <span class="text-xs mt-1">Search</span>
        </button>
        <button class="text-gray-500 flex flex-col items-center">
          <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
          <span class="text-xs mt-1">Message</span>
        </button>
        <button class="text-gray-500 flex flex-col items-center">
          <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
          <span class="text-xs mt-1">Settings</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      matchingList: [
        {
          name: 'Sleeping Bear',
          matchRate: 95,
          image: '/images/sleeping-bear.jpg'
        },
        { name: 'Crying Turtle', matchRate: 93, image: null },
        { name: 'Running Rabbit', matchRate: 88, image: null },
        { name: 'Rising Star', matchRate: 88, image: null },
        { name: 'Tired Hunter', matchRate: 77, image: null },
        { name: 'Angry Bird', matchRate: 63, image: null }
      ]
    };
  },
  head() {
    return {
      title: 'Matching List - SKKU-Dormie'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
