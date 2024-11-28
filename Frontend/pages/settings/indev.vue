<template>
  <div class="flex flex-col min-h-screen bg-gray-100">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Settings</h1>
    </div>

    <!-- Profile Section -->
    <div class="flex flex-col items-center mt-8">
      <div class="relative">
        <div class="w-24 h-24 rounded-full overflow-hidden bg-gray-300">
          <!-- <img
              src="/images/hungry-donut.jpg"
              alt="Profile"
              class="w-full h-full object-cover"
            /> -->
        </div>
        <button
          class="absolute bottom-1 right-1 bg-black text-white w-6 h-6 rounded-full flex items-center justify-center"
        >
          +
        </button>
      </div>
      <div class="mt-4 w-3/4">
        <label for="username" class="block text-sm font-medium text-gray-600">
          Username*
        </label>
        <div class="relative mt-1">
          <input
            id="username"
            type="text"
            value="Hungry Donut"
            class="w-full border border-gray-300 rounded-md px-3 py-2 text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="button"
            class="absolute top-2 right-2 bg-gray-100 text-blue-500 p-1 rounded-full hover:bg-gray-200"
          >
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
                d="M4.318 2.318a2.25 2.25 0 013.182 0L12 6.82l4.5-4.5a2.25 2.25 0 013.182 3.182l-4.5 4.5L20 16.318a2.25 2.25 0 01-3.182 3.182l-4.5-4.5-4.5 4.5a2.25 2.25 0 01-3.182-3.182l4.5-4.5-4.5-4.5a2.25 2.25 0 010-3.182z"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Buttons -->
    <div class="mt-8 px-6 space-y-4">
      <button
        class="w-full bg-blue-500 text-white py-3 rounded-lg text-sm font-medium hover:bg-blue-600"
      >
        My Information
      </button>
      <button
        class="w-full bg-gray-200 text-gray-800 py-3 rounded-lg text-sm font-medium hover:bg-gray-300"
      >
        Account Setting
      </button>
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
  head() {
    return {
      title: 'Settings - SKKU-Dormie'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
