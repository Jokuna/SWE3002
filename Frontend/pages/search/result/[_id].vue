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
      <div>
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
                  Matching Rate: {{ item.similarity }}%
                </p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <NuxtLink :to="`/profile/${item._id.$oid}`">
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

const messages = ref([]);

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

async function getData() {
  const user_id = await getUser_id();

  const data = await $fetch(`/backend/search/filter?user_id=${user_id}`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
  });

  console.log(data);

  messages.value = data;

  console.log(messages.value);
}

getData();
</script>

<style>
/* Optional custom styles */
</style>
