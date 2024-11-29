<template>
  <div class="flex flex-col min-h-screen bg-gray-100">
    <!-- Tabs Navigation -->
    <div class="flex border-b bg-white">
      <button
        class="flex-1 py-2 text-gray-500 border-b-2 border-transparent hover:text-blue-500"
      >
        Basic Info
      </button>
      <button
        class="flex-1 py-2 text-blue-500 border-b-2 border-blue-500 font-medium"
      >
        Sleep Time
      </button>
      <button
        class="flex-1 py-2 text-gray-500 border-b-2 border-transparent hover:text-blue-500"
      >
        Extra
      </button>
    </div>

    <!-- Content Section -->
    <div class="flex flex-col items-center justify-center flex-1 px-6 py-8">
      <!-- Sleep At and Wake Up Fields -->
      <div class="grid grid-cols-2 gap-6 mb-6 w-full">
        <div>
          <label
            for="sleepAt"
            class="block text-sm font-medium text-gray-600 mb-2"
          >
            Sleep At
          </label>
          <input
            id="sleepAt"
            type="number"
            min="0"
            max="23"
            placeholder="23"
            class="w-full border border-gray-300 rounded-md px-4 py-2 text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <div>
          <label
            for="wakeUp"
            class="block text-sm font-medium text-gray-600 mb-2"
          >
            Wake up...
          </label>
          <input
            id="wakeUp"
            type="number"
            min="0"
            max="23"
            placeholder="08"
            class="w-full border border-gray-300 rounded-md px-4 py-2 text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
      </div>

      <!-- Buttons -->
      <div class="flex space-x-4">
        <button
          class="w-24 bg-gray-300 text-gray-700 py-2 rounded-md text-sm font-medium hover:bg-gray-400"
        >
          Reset
        </button>
        <button
          class="w-24 bg-blue-500 text-white py-2 rounded-md text-sm font-medium hover:bg-blue-600"
        >
          Apply
        </button>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="flex justify-around border-t bg-white py-4 mt-auto">
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
      sleepAt: 23,
      wakeUp: 8
    };
  },
  methods: {
    resetFields() {
      this.sleepAt = 23;
      this.wakeUp = 8;
    },
    applySettings() {
      console.log(`Sleep At: ${this.sleepAt}, Wake Up: ${this.wakeUp}`);
    }
  },
  head() {
    return {
      title: 'Sleep Time - SKKU-Dormie'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
