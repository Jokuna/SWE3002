<template>
  <div class="flex flex-col min-h-screen bg-white">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white" style="max-height: 60px">
      <h1 class="text-xl font-bold text-gray-800">Sleeping Bear</h1>
    </div>

    <!-- Chat Section -->
    <div
      class="flex-1 overflow-y-auto px-4 py-4 bg-gray-100"
      style="max-height: calc(100vh - 180px)"
    >
      <!-- Timestamp -->
      <p class="text-center text-gray-500 text-xs mb-4">10:30</p>

      <!-- V-for -->
      <div v-for="(message, index) in dataSource" :key="index">
        <div
          v-if="user_id != message.writerId.$id.$oid"
          class="flex items-start space-x-2 mb-4"
        >
          <!-- 아바타 -->
          <img
            :src="message.avatar || 'https://via.placeholder.com/40'"
            alt="Avatar"
            class="w-10 h-10 rounded-full"
          />

          <!-- 메시지 내용 -->
          <div class="bg-blue-100 text-blue-800 p-3 rounded-lg max-w-xs">
            <p>{{ message.text }}</p>
          </div>
        </div>

        <div v-else class="flex items-start justify-end space-x-2 mb-4">
          <div class="bg-gray-300 text-gray-800 p-3 rounded-lg max-w-xs">
            <p>{{ message.text }}</p>
          </div>
          <img
            src="https://via.placeholder.com/40"
            alt="Avatar"
            class="w-10 h-10 rounded-full"
          />
        </div>
      </div>
    </div>

    <!-- Input Section -->
    <div class="flex items-center px-4 py-2 border-t bg-white">
      <input
        type="text"
        v-model="txt"
        placeholder="Say something..."
        class="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none"
      />

      <button
        class="ml-2"
        style="
          background-color: #007bff;
          border: none;
          padding: 10px;
          border-radius: 50%;
          cursor: pointer;
          display: flex;
          justify-content: center;
          align-items: center;
        "
        @click="sendChatMessage"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="white"
          style="width: 20px; height: 20px"
        >
          <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" />
        </svg>
      </button>
    </div>

    <!-- Bottom Navigation -->
    <div class="flex justify-around border-t bg-white py-2">
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

<script setup>
import { onMounted, onUnmounted, ref, watch, nextTick } from 'vue';
import { useRoute } from 'vue-router';
import { useNuxtApp } from '#app';

const { $store } = useNuxtApp();

const route = useRoute();
const chatroom_id = computed(() => route.params._id);

console.log(chatroom_id.value);

const dataSource = ref([]);
const user_id = ref('');
const txt = ref('');

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
  if ($store.state.token == '') {
    return;
  }
  const data = await decodeJwt($store.state.token);
  user_id.value = data;
  return data;
}

const getHistory = async (chatroom_id) => {
  const data = await $fetch(`/backend/chat/history/${chatroom_id}`, {
    headers: {
      accept: 'application/json'
    },
    method: 'GET'
  });

  dataSource.value = data;
};

const sendChatMessage = async () => {
  const data = await $fetch(
    `/backend/chat/message/${route.params._id}?msg=${txt.value}`,
    {
      headers: {
        accept: 'application/json'
      },
      method: 'POST',
      body: JSON.stringify({
        token: $store.state.token,
        username: 'dummy'
      })
    }
  );

  console.log(data);

  // 채팅창 reload
  getHistory(route.params._id);
};

getUser_id();
getHistory(chatroom_id.value);
console.log(dataSource);
console.log(dataSource.value);

onMounted(() => {});
</script>
