<template>
  <div class="flex flex-col min-h-screen bg-white">
    <!-- Header -->
    <!-- <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Details</h1>
    </div> -->

    <!-- Scrollable Content -->
    <div
      class="flex-1 overflow-y-auto px-6 py-4"
      style="max-height: calc(100vh - 150px)"
    >
      <!-- Profile Section -->
      <div class="flex flex-col items-center mb-6">
        <div class="w-24 h-24 rounded-full bg-gray-300 overflow-hidden">
          <!-- Placeholder for Profile Image -->
        </div>
        <p class="mt-4 text-lg font-medium text-gray-800">
          Hi, I&apos;m {{ dataProfile.username }}.
        </p>
        <p class="text-gray-600">I am :</p>
      </div>

      <!-- Details Section -->
      <div class="space-y-3">
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">
            Gender is {{ dataProfile_info.isMale ? 'Male' : 'Female' }}
          </p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">
            I would like to live in
            {{
              dataProfile_info.dormitary == 1
                ? 'In-kwan'
                : dataProfile_info.dormitary == 2
                  ? 'Ui-kwan'
                  : dataProfile_info.dormitary == 3
                    ? 'Ye-kwan'
                    : dataProfile_info.dormitary == 4
                      ? 'Ji-kwan'
                      : 'Sin-kwan'
            }}
          </p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">
            I am {{ dataProfile_info.isSmoke ? 'Smoker' : 'not Smoker' }}
          </p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">Not in Dormitory in weekend</p>
          <!-- {{ dataProfile_info.weekendProportion }} -->
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">
            Bedtime is {{ dataProfile_info.sleepingTime }} ~
            {{ dataProfile_info.wakeTime }}
          </p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">
            Age is
            {{ dataProfile_info.age == 0 ? 'private' : dataProfile_info.age }}
          </p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">
            Major is
            {{
              dataProfile_info.major == '' ? 'private' : dataProfile_info.major
            }}
          </p>
        </div>
      </div>
    </div>

    <!-- Action Button -->
    <div class="px-6 py-4">
      <button
        type="button"
        @click="createChatRoom"
        class="w-full bg-blue-500 text-white py-3 rounded text-sm font-medium hover:bg-blue-600"
      >
        Gonna chat with her/him
      </button>
    </div>

    <!-- Bottom Navigation -->
    <div
      class="flex justify-around border-t bg-white py-4"
      style="padding-bottom: 0"
    >
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
import { useRoute } from 'vue-router';
import { useNuxtApp } from '#app';

const { $store } = useNuxtApp();

const route = useRoute();
const dataProfile = ref([]);
const dataProfile_info = ref([]);

const getprofile = async () => {
  const data = await $fetch(`/backend/user/profile/${route.params._id}`, {
    headers: {
      accept: 'application/json'
    },
    method: 'GET'
  });

  console.log(data);
  dataProfile.value = data;

  // 추가로, user info 가져오는 기능 구현
  const datainfo = await $fetch(
    `/backend/user/profile/info/${route.params._id}`,
    {
      headers: {
        accept: 'application/json'
      },
      method: 'GET'
    }
  );

  dataProfile_info.value = datainfo;
  // userId
};

const createChatRoom = async () => {
  // 채팅방 생성

  const data = await $fetch(
    `/backend/chat/create?target_user_id=${dataProfile.value._id}`,
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

  const { chatroom_id } = data;

  // 채팅방 이동
  await navigateTo(`/chat/${chatroom_id}`);
};

getprofile();
</script>
