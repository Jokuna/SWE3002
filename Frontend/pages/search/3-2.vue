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
        <NuxtLink to="/search/1"> Basic Info </NuxtLink>
      </button>
      <button
        class="flex-1 py-2 text-gray-500 border-b-2 border-transparent hover:text-blue-500"
      >
        <NuxtLink to="/search/2"> Sleep Time </NuxtLink>
      </button>
      <button
        class="flex-1 py-2 text-blue-500 border-b-2 border-blue-500 font-medium"
      >
        <NuxtLink to="/search/3"> Extra </NuxtLink>
      </button>
    </div>

    <!-- Content Section -->
    <div class="flex-1 bg-white overflow-y-auto">
      <div>
        <div class="grid grid-cols-[3fr_7fr] grid-rows-2 h-full w-full">
          <!-- Labels (Left Column) -->
          <div
            class="font-medium text-gray-700 h-12 p-4 bg-gray-100 flex items-center"
            style="height: 100%"
          >
            <NuxtLink to="/search/3-1">Age</NuxtLink>
          </div>
          <!-- Radio buttons for Gender -->
          <div class="items-center space-x-4 w-full h-full">
            <label
              class="flex items-center space-x-2 justify-between w-full h-full p-4"
            >
              <input
                id="major"
                type="string"
                placeholder="write your major"
                v-model="major"
                class="w-full border border-gray-300 rounded-md px-4 py-2 text-center focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </label>
          </div>

          <div
            class="font-medium text-gray-700 h-12 p-4 flex items-center"
            style="height: 100%"
          >
            <NuxtLink to="/search/3-2">Major</NuxtLink>
          </div>

          <div class="items-center space-x-4 w-full h-full"></div>

          <!-- Buttons Row -->
          <div class="col-span-2 flex justify-between mt-6 p-2">
            <button
              class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg w-2/5"
            >
              Reset
            </button>
            <button
              class="px-4 py-2 bg-blue-600 text-white rounded-lg w-2/5"
              @click="set_filter"
            >
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

const major = ref('');

watchEffect(() => {
  console.log(`Current major at: ${major.value}`);

  let filterData = store.getters.getFilterData;

  filterData.major = major.value;
  store.dispatch('updateFilterData', filterData);

  console.log(store.getters.getFilterData);
});

// -- filter 업로드 부분
async function decodeJwt(token) {
  const result = await $fetch(`/backend/chat/jwt?token=${token}`, {
    headers: {
      accept: 'application/json'
    },
    method: 'GET'
  });
  const { sub } = result;
  return sub;
}

async function getUser_id() {
  if (store.getters.getToken == '') {
    return;
  }
  const data = await decodeJwt(store.getters.getToken);
  // console.log(data);
  return data;
}

async function set_filter() {
  // console.log(store.getters.getFilterData)

  const user_id = await getUser_id();

  const user_info = {
    ...store.getters.getFilterData,
    user_id
  };

  await navigateTo(`/search/result/${user_id}`); // user_id
}
</script>

<style>
/* Optional custom styles */
</style>
