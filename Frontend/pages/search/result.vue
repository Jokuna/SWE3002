<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <!-- Header -->
    <!-- <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Message Box</h1>
    </div> -->

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
    <div class="flex-1 bg-white overflow-y-auto p-4">
      <div v-if="selectedTab === 'Basic Info'">
        <ul class="space-y-2">
          <li v-for="(item, index) in messages" :key="index">
            <p class="text-gray-800 font-medium">{{ item.name }}</p>
            <p class="text-sm text-gray-500">
              Matching Rate: {{ item.matchRate }}%
            </p>
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
          <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
          <span class="text-xs mt-1">Search</span>
        </button>
      </NuxtLink>

      <NuxtLink to="/chat">
        <button class="text-blue-500 flex flex-col items-center">
          <div class="w-6 h-6 bg-blue-500 rounded-full"></div>
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
        { name: 'Sleeping Bear', matchRate: 95 },
        { name: 'Crying Turtle', matchRate: 93 },
        { name: 'Running Rabbit', matchRate: 88 },
        { name: 'Rising Star', matchRate: 88 },
        { name: 'Tired Hunter', matchRate: 77 },
        { name: 'Angry Bird', matchRate: 63 }
      ],
      sleepTimes: [
        { name: 'Sleeping Bear', bedtime: '10:00 PM' },
        { name: 'Crying Turtle', bedtime: '11:30 PM' },
        { name: 'Running Rabbit', bedtime: '9:30 PM' },
        { name: 'Rising Star', bedtime: '12:00 AM' },
        { name: 'Tired Hunter', bedtime: '1:00 AM' },
        { name: 'Angry Bird', bedtime: '2:00 AM' }
      ],
      extras: [
        { name: 'Sleeping Bear', habit: 'Reads books before bed' },
        { name: 'Crying Turtle', habit: 'Watches TV late' },
        { name: 'Running Rabbit', habit: 'Goes jogging in the morning' },
        { name: 'Rising Star', habit: 'Plays video games' },
        { name: 'Tired Hunter', habit: 'Sleeps late after work' },
        { name: 'Angry Bird', habit: 'Eats midnight snacks' }
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
