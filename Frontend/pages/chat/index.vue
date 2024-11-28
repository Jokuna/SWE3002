<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Message Box</h1>
    </div>

    <!-- Message List -->
    <div class="flex-1 bg-white overflow-y-auto">
      <ul class="divide-y divide-gray-200">
        <li
          v-for="(item, index) in messages"
          :key="index"
          class="flex items-center justify-between px-6 py-4 hover:bg-gray-50 cursor-pointer"
        >
          <div class="flex items-center space-x-4">
            <div class="w-10 h-10 bg-gray-300 rounded-full"></div>
            <div>
              <p class="text-gray-800 font-medium">{{ item.name }}</p>
              <p class="text-sm text-gray-500">
                Matching Rate: {{ item.matchRate }}%
              </p>
            </div>
          </div>
          <div class="flex items-center space-x-2">
            <span
              v-if="item.unread"
              class="w-2 h-2 bg-red-500 rounded-full"
              title="Unread Message"
            ></span>
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
          </div>
        </li>
      </ul>
    </div>

    <!-- Bottom Navigation -->
    <div class="flex justify-around border-t bg-white py-4">
      <button class="text-gray-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
        <span class="text-xs mt-1">Search</span>
      </button>
      <button class="text-blue-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-blue-500 rounded-full"></div>
        <span class="text-xs mt-1">Message</span>
      </button>
      <button class="text-gray-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
        <span class="text-xs mt-1">Settings</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [
        { name: 'Sleeping Bear', matchRate: 95, unread: true },
        { name: 'Crying Turtle', matchRate: 93, unread: false },
        { name: 'Running Rabbit', matchRate: 88, unread: false },
        { name: 'Rising Star', matchRate: 88, unread: false },
        { name: 'Tired Hunter', matchRate: 77, unread: false },
        { name: 'Angry Bird', matchRate: 63, unread: false }
      ]
    };
  },
  head() {
    return {
      title: 'Message Box - SKKU-Dormie'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
