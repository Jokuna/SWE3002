<template>
  <div class="flex flex-col min-h-screen bg-gray-100">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Search Page 1</h1>
    </div>

    <!-- Tabs Navigation -->
    <div class="flex border-b bg-white">
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

    <!-- Content Section -->
    <div class="flex flex-col items-center justify-center flex-1 px-6 py-8">
      <div class="w-full max-w-md space-y-6">
        <!-- Gender -->
        <div>
          <label class="block text-sm font-medium text-gray-600">Gender</label>
          <div class="mt-2 space-y-2">
            <div class="flex items-center">
              <input
                id="gender-male"
                name="gender"
                type="radio"
                class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500"
              />
              <label for="gender-male" class="ml-3 text-gray-700">Male</label>
            </div>
            <div class="flex items-center">
              <input
                id="gender-female"
                name="gender"
                type="radio"
                class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500"
              />
              <label for="gender-female" class="ml-3 text-gray-700"
                >Female</label
              >
            </div>
          </div>
        </div>

        <!-- Dormitory -->
        <div>
          <label class="block text-sm font-medium text-gray-600"
            >Dormitory</label
          >
          <div class="mt-2 space-y-2">
            <div class="flex items-center">
              <input
                id="dorm-ui-kwan"
                name="dormitory"
                type="radio"
                class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500"
                checked
              />
              <label for="dorm-ui-kwan" class="ml-3 text-gray-700"
                >Ui-kwan</label
              >
            </div>
            <div class="flex items-center">
              <input
                id="dorm-ye-kwan"
                name="dormitory"
                type="radio"
                class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500"
                checked
              />
              <label for="dorm-ye-kwan" class="ml-3 text-gray-700"
                >Ye-kwan</label
              >
            </div>
          </div>
        </div>

        <!-- Smoking Status -->
        <div>
          <label class="block text-sm font-medium text-gray-600"
            >Smoking Stat.</label
          >
          <div class="mt-2 space-y-2">
            <div class="flex items-center">
              <input
                id="smoking-yes"
                name="smoking"
                type="radio"
                class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500"
              />
              <label for="smoking-yes" class="ml-3 text-gray-700">Yes</label>
            </div>
            <div class="flex items-center">
              <input
                id="smoking-no"
                name="smoking"
                type="radio"
                class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500"
              />
              <label for="smoking-no" class="ml-3 text-gray-700">No</label>
            </div>
          </div>
        </div>

        <!-- Proportion -->
        <div>
          <label class="block text-sm font-medium text-gray-600"
            >Proportion</label
          >
          <div class="mt-2 space-y-2">
            <div class="flex items-center">
              <input
                id="proportion-jikwan"
                name="proportion"
                type="radio"
                class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500"
              />
              <label for="proportion-jikwan" class="ml-3 text-gray-700"
                >Ji-kwan</label
              >
            </div>
            <div class="flex items-center">
              <input
                id="proportion-sinkwan"
                name="proportion"
                type="radio"
                class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500"
              />
              <label for="proportion-sinkwan" class="ml-3 text-gray-700"
                >Sin-kwan</label
              >
            </div>
          </div>
        </div>

        <!-- Buttons -->
        <div class="flex space-x-4">
          <button
            type="button"
            class="w-24 bg-gray-300 text-gray-700 py-2 rounded-md text-sm font-medium hover:bg-gray-400"
          >
            Reset
          </button>
          <button
            type="button"
            class="w-24 bg-blue-500 text-white py-2 rounded-md text-sm font-medium hover:bg-blue-600"
          >
            Apply
          </button>
        </div>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="flex justify-around border-t bg-white py-4 mt-auto">
      <button class="text-blue-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-blue-500 rounded-full"></div>
        <span class="text-xs mt-1">Search</span>
      </button>
      <button class="text-gray-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
        <span class="text-xs mt-1">Picture</span>
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
  head() {
    return {
      title: 'Search Page 1 - SKKU-Dormie'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
