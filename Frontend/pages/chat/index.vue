<template>
  <div class="flex flex-col h-screen bg-gray-100">
    <!-- Header -->
    <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Message Box</h1>
    </div>

    <!-- Message List -->
    <div class="flex-1 bg-white overflow-y-auto">
      <ul class="divide-y divide-gray-200">
        <li
          v-for="(item, index) in messages"
          :key="index"
          class="flex items-center justify-between px-6 py-4 hover:bg-gray-50 cursor-pointer"
        >
          <div class="flex items-center space-x-4">
            <div class="w-10 h-10 bg-gray-300 rounded-full"></div>
            <div>
              <p class="text-gray-800 font-medium">{{ item.username }}</p>
            </div>
          </div>
          <div class="flex items-center space-x-2">
            <NuxtLink :to="`/chat/${item.chatRoomId}`">
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

<script setup>
import { ref } from 'vue';
import { useNuxtApp } from '#app';

const { $store } = useNuxtApp();

// const messages = ref([
//   { username: 'Sleeping Bear', matchRate: 95, unread: true },
//   { username: 'Crying Turtle', matchRate: 93, unread: false },
//   { username: 'Running Rabbit', matchRate: 88, unread: false },
//   { username: 'Rising Star', matchRate: 88, unread: false },
//   { username: 'Tired Hunter', matchRate: 77, unread: false },
//   { username: 'Angry Bird', matchRate: 63, unread: false }
// ]);

const messages = ref([]);
const user_id = ref('');

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

getUser_id();

const getChatRoomList = async (chatroom_id) => {
  const data = await $fetch(`/backend/chat/list`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      token: $store.state.token,
      username: 'dummy'
    })
  });

  console.log(data);

  for (const iterator of data) {
    console.log(iterator);

    console.log(iterator.userId1);
    console.log(iterator.userId2);
    console.log(user_id.value);

    let target_user_id = iterator.userId1;
    if (iterator.userId1 == user_id.value) {
      target_user_id = iterator.userId2;
    }

    const user = await $fetch(`/backend/user/profile/${target_user_id}`, {
      headers: {
        accept: 'application/json'
      },
      method: 'GET'
    });

    console.log(iterator);
    console.log(user);

    messages.value.push({
      ...iterator,
      ...user
    });
  }
  console.log(messages.value);
};

getChatRoomList();
</script>

<style>
/* Optional custom styles */
</style>
