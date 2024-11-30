<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Search</h1>
    </div>

    <!-- Tabs -->
    <div class="flex border-b">
      <button
        class="flex-1 py-2 text-blue-500 border-b-2 border-blue-500 font-medium"
      >
        <NuxtLink to="/search/1"> Basic Info </NuxtLink>
      </button>
      <button
        class="flex-1 py-2 text-gray-500 border-b-2 border-transparent hover:text-blue-500"
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
    <div class="flex-1 bg-white overflow-y-auto">
      <div>
        <div class="grid grid-cols-[3fr_7fr] grid-rows-5 h-full w-full">
          <!-- Labels (Left Column) -->
          <div
            class="font-medium text-gray-700 h-12 bg-gray-100 p-4 flex items-center"
            style="height: 100%"
          >
            <NuxtLink to="/search/1-1">Gender</NuxtLink>
          </div>
          <!-- Radio buttons for Gender -->
          <div class="items-center space-x-4 w-full h-full">
            <label
              class="flex items-center space-x-2 justify-between w-full h-full p-4"
            >
              <span>Yes</span>
              <input
                type="radio"
                name="smoke"
                value="true"
                v-model="smoke"
                class="form-radio text-blue-600"
              />
            </label>
          </div>

          <div
            class="font-medium text-gray-700 h-12 bg-gray-100 p-4 flex items-center"
            style="height: 100%"
          >
            <NuxtLink to="/search/1-2">Dormitory</NuxtLink>
          </div>

          <!-- Radio buttons for Dormitory -->
          <div class="items-center space-x-4 w-full h-full">
            <label
              class="flex items-center space-x-2 justify-between w-full h-full p-4"
            >
              <span>No</span>
              <input
                type="radio"
                name="smoke"
                value="false"
                v-model="smoke"
                class="form-radio text-blue-600"
              />
            </label>
          </div>

          <div
            class="font-medium text-gray-700 h-12 p-4 flex items-center"
            style="height: 100%"
          >
            <NuxtLink to="/search/1-3">Smoking Stat.</NuxtLink>
          </div>

          <!-- Radio buttons for Smoking Status -->
          <div class="items-center space-x-4 w-full h-full">
            <label
              class="flex items-center space-x-2 justify-between w-full h-full p-4"
            >
            </label>
          </div>

          <div
            class="font-medium text-gray-700 h-12 bg-gray-100 p-4 flex items-center"
            style="height: 100%"
          >
            <NuxtLink to="/search/1-4">Proportion </NuxtLink>
          </div>
          <!-- Radio buttons for Proportion -->
          <div class="items-center space-x-4 w-full h-full">
            <label
              class="flex items-center space-x-2 justify-between w-full h-full p-4"
            >
            </label>
          </div>

          <div
            class="font-medium text-gray-700 h-12 bg-gray-100 p-4"
            style="height: 100%"
          ></div>

          <!-- Radio buttons for Smoking Status -->
          <div class="items-center space-x-4 w-full h-full">
            <label
              class="flex items-center space-x-2 justify-between w-full h-full p-4"
            >
            </label>
          </div>

          <!-- Buttons Row -->
          <div class="col-span-2 flex justify-between mt-6 p-2">
            <button
              class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg w-2/5"
            >
              Reset
            </button>
            <button class="px-4 py-2 bg-blue-600 text-white rounded-lg w-2/5">
              Apply
            </button>
          </div>
        </div>
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

<script setup>
import { ref, watch } from 'vue';
import { useStore } from 'vuex';

const store = useStore();

const smoke = ref(false);

watchEffect(() => {
  console.log(`Current smoke: ${smoke.value}`);
  // 실시간으로 Vuex에 저장

  let filterData = store.getters.getFilterData;

  filterData.isSmoke = smoke.value == 'true'; // string이라..
  store.dispatch('updateFilterData', filterData);
});
</script>

<style>
/* Optional custom styles */
</style>
