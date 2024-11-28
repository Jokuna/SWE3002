<template>
  <div
    class="flex flex-col items-center justify-center min-h-screen bg-gray-100"
  >
    <div class="w-full max-w-md bg-white rounded-lg shadow-md p-6">
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

      <!-- Form Content -->
      <form class="mt-4 space-y-4">
        <!-- Gender -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Gender</label>
          <div class="mt-2 space-y-2">
            <div>
              <input id="gender1" type="radio" name="gender" class="mr-2" />
              <label for="gender1" class="text-gray-700">In-kwan</label>
            </div>
          </div>
        </div>

        <!-- Dormitory -->
        <div>
          <label class="block text-sm font-medium text-gray-700"
            >Dormitory</label
          >
          <div class="mt-2 space-y-2">
            <div>
              <input id="dorm1" type="radio" name="dormitory" class="mr-2" />
              <label for="dorm1" class="text-gray-700">Ui-kwan</label>
            </div>
            <div>
              <input id="dorm2" type="radio" name="dormitory" class="mr-2" />
              <label for="dorm2" class="text-gray-700">Ye-kwan</label>
            </div>
          </div>
        </div>

        <!-- Smoking Status -->
        <div>
          <label class="block text-sm font-medium text-gray-700"
            >Smoking Stat.</label
          >
          <div class="mt-2 space-y-2">
            <div>
              <input id="smoking1" type="radio" name="smoking" class="mr-2" />
              <label for="smoking1" class="text-gray-700">Ye-kwan</label>
            </div>
          </div>
        </div>

        <!-- Proportion -->
        <div>
          <label class="block text-sm font-medium text-gray-700"
            >Proportion</label
          >
          <div class="mt-2 space-y-2">
            <div>
              <input id="prop1" type="radio" name="proportion" class="mr-2" />
              <label for="prop1" class="text-gray-700">Ji-kwan</label>
            </div>
            <div>
              <input id="prop2" type="radio" name="proportion" class="mr-2" />
              <label for="prop2" class="text-gray-700">Sin-kwan</label>
            </div>
          </div>
        </div>

        <!-- Buttons -->
        <div class="flex justify-between mt-4">
          <button
            type="button"
            class="w-24 bg-gray-300 text-gray-700 py-2 rounded-md text-sm font-medium hover:bg-gray-400"
          >
            Reset
          </button>
          <button
            type="submit"
            class="w-24 bg-blue-500 text-white py-2 rounded-md text-sm font-medium hover:bg-blue-600"
          >
            Apply
          </button>
        </div>
      </form>

      <!-- Bottom Navigation -->
      <div class="flex justify-around border-t mt-6 pt-4">
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
