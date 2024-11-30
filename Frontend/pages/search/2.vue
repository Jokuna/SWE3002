<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Search</h1>
    </div>

    <!-- Tabs -->
    <div class="flex border-b">
      <button
        class="flex-1 py-2 text-gray-500 border-b-2 border-transparent hover:text-blue-500"
      >
        <NuxtLink to="/search/1-1"> Basic Info </NuxtLink>
      </button>
      <button
        class="flex-1 py-2 text-blue-500 border-b-2 border-blue-500 font-medium"
      >
        <NuxtLink to="/search/2"> Sleep Time </NuxtLink>
      </button>
      <button
        class="flex-1 py-2 text-gray-500 border-b-2 border-transparent hover:text-blue-500"
      >
        <NuxtLink to="/search/3"> Extra </NuxtLink>
      </button>
    </div>

    <!-- Content Section -->

    <div
      class="flex flex-col items-center flex-1 py-8 bg-white overflow-y-auto"
    >
      <!-- Sleep At and Wake Up Fields -->
      <div class="grid grid-cols-2 gap-6 mb-6 w-full px-4">
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
      <div class="flex space-x-4 justify-between w-full px-4">
        <button
          class="bg-gray-200 text-gray-700 py-2 rounded-md text-sm font-medium hover:bg-gray-400 w-2/5"
        >
          Reset
        </button>
        <button
          class="bg-blue-500 text-white py-2 rounded-md text-sm font-medium hover:bg-blue-600 w-2/5"
        >
          Apply
        </button>
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

<script></script>

<style>
/* Optional custom styles */
</style>
