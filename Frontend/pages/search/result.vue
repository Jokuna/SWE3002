<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Search</h1>
    </div>

    <!-- Tabs -->
    <div class="flex border-b">
      <button
        class="flex-1 py-2"
        :class="
          selectedTab === 'Basic Info'
            ? 'text-blue-500 border-b-2 border-blue-500 font-medium'
            : 'text-gray-500 border-b-2 border-transparent hover:text-blue-500'
        "
        @click="selectedTab = 'Basic Info'"
      >
        Basic Info
      </button>
      <button
        class="flex-1 py-2"
        :class="
          selectedTab === 'Sleep Time'
            ? 'text-blue-500 border-b-2 border-blue-500 font-medium'
            : 'text-gray-500 border-b-2 border-transparent hover:text-blue-500'
        "
        @click="selectedTab = 'Sleep Time'"
      >
        Sleep Time
      </button>
      <button
        class="flex-1 py-2"
        :class="
          selectedTab === 'Extra'
            ? 'text-blue-500 border-b-2 border-blue-500 font-medium'
            : 'text-gray-500 border-b-2 border-transparent hover:text-blue-500'
        "
        @click="selectedTab = 'Extra'"
      >
        Extra
      </button>
    </div>

    <!-- Content Section -->
    <div class="flex-1 bg-white overflow-y-auto">
      <div v-if="selectedTab === 'Basic Info'">
        <ul class="space-y-2">
          <li
            v-for="(item, index) in messages"
            :key="index"
            class="flex items-center justify-between px-6 py-4 hover:bg-gray-50 cursor-pointer"
          >
            <div class="flex items-center space-x-4">
              <div class="w-10 h-10 bg-gray-300 rounded-full"></div>
              <div>
                <p class="text-gray-800 font-medium">{{ item.username }}</p>
                <p class="text-sm text-gray-500">
                  Matching Rate: {{ item.matchRate }}%
                </p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <NuxtLink :to="`/profile/${item.user_id}`">
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
              </NuxtLink>
            </div>
          </li>
        </ul>
      </div>
      <div v-else-if="selectedTab === 'Sleep Time'">
        <ul class="space-y-2">
          <li v-for="(item, index) in sleepTimes" :key="index">
            <p class="text-gray-800 font-medium">{{ item.name }}</p>
            <p class="text-sm text-gray-500">Bedtime: {{ item.bedtime }}</p>
          </li>
        </ul>
      </div>
      <div v-else-if="selectedTab === 'Extra'">
        <ul class="space-y-2">
          <li v-for="(item, index) in extras" :key="index">
            <p class="text-gray-800 font-medium">{{ item.name }}</p>
            <p class="text-sm text-gray-500">Habit: {{ item.habit }}</p>
          </li>
        </ul>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="flex justify-around border-t bg-white py-4">
      <NuxtLink to="/search">
        <button class="text-gray-500 flex flex-col items-center">
          <div class="w-6 h-6 bg-blue-500 rounded-full"></div>
          <span class="text-xs mt-1">Search</span>
        </button>
      </NuxtLink>

      <NuxtLink to="/chat">
        <button class="text-blue-500 flex flex-col items-center">
          <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
          <span class="text-xs mt-1">Message</span>
        </button>
      </NuxtLink>
      <NuxtLink to="/settings">
        <button class="text-gray-500 flex flex-col items-center">
          <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
          <span class="text-xs mt-1">Settings</span>
        </button>
      </NuxtLink>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedTab: 'Basic Info',
      messages: [
        { username: 'Sleeping Bear', matchRate: 95 },
        { username: 'Crying Turtle', matchRate: 93 },
        { username: 'Running Rabbit', matchRate: 88 },
        { username: 'Rising Star', matchRate: 88 },
        { username: 'Tired Hunter', matchRate: 77 },
        { username: 'Angry Bird', matchRate: 63 }
      ],
      sleepTimes: [
        { username: 'Sleeping Bear', bedtime: '10:00 PM' },
        { username: 'Crying Turtle', bedtime: '11:30 PM' },
        { username: 'Running Rabbit', bedtime: '9:30 PM' },
        { username: 'Rising Star', bedtime: '12:00 AM' },
        { username: 'Tired Hunter', bedtime: '1:00 AM' },
        { username: 'Angry Bird', bedtime: '2:00 AM' }
      ],
      extras: [
        { username: 'Sleeping Bear', habit: 'Reads books before bed' },
        { username: 'Crying Turtle', habit: 'Watches TV late' },
        { username: 'Running Rabbit', habit: 'Goes jogging in the morning' },
        { username: 'Rising Star', habit: 'Plays video games' },
        { username: 'Tired Hunter', habit: 'Sleeps late after work' },
        { username: 'Angry Bird', habit: 'Eats midnight snacks' }
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
