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
          Username
        </label>
        <div class="relative mt-1">
          <input
            id="username"
            type="text"
            v-model="user_name"
            class="w-full border border-gray-300 rounded-md px-3 py-2 text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="button"
            @click="generateRandomNickname"
            class="absolute top-2 right-2 bg-gray-100 text-blue-500 p-1 rounded-full hover:bg-gray-200"
          >
            <div
              class="flex items-center justify-center w-4 h-4 rounded-full bg-blue-100 text-blue-500 text-sm font-bold"
            >
              ↺
            </div>
            <!-- <svg
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
            </svg> -->
          </button>
        </div>
      </div>
    </div>

    <!-- Buttons -->
    <div class="mt-8 px-6 space-y-4">
      <button
        @click="update_user_name"
        class="w-full bg-blue-500 text-white py-3 rounded-lg text-sm font-medium hover:bg-blue-600"
      >
        Update
      </button>
      <button
        class="w-full bg-gray-200 text-gray-800 py-3 rounded-lg text-sm font-medium hover:bg-gray-300"
      >
        <NuxtLink to="/settings/myinfo"> Account Setting </NuxtLink>
      </button>
    </div>

    <!-- Bottom Navigation -->
    <div class="flex justify-around border-t bg-white py-4 mt-auto">
      <NuxtLink to="/search">
        <button class="text-gray-500 flex flex-col items-center">
          <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
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
          <div class="w-6 h-6 bg-blue-500 rounded-full"></div>
          <span class="text-xs mt-1">Settings</span>
        </button>
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { useNuxtApp } from '#app';

const { $store } = useNuxtApp();
const user_name = ref('');

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
  console.log(data);
  return data;
}

async function get_user_info() {
  const user_id = await getUser_id();
  console.log(user_id);
  console.log($store.state.token);

  const user = await $fetch(`/backend/user/profile/${user_id}`, {
    headers: {
      accept: 'application/json'
    },
    method: 'GET'
  });

  user_name.value = user.username;
}
function generateRandomNickname() {
  const 명사목록 = [
    // 자연 관련 명사
    '바다',
    '하늘',
    '나무',
    '꽃',
    '돌',
    '산',
    '강',
    '구름',
    '별',
    '달',
    '햇빛',
    '숲',
    '바람',
    '새',
    '호수',
    '노을',
    '풀',
    '샘',
    '파도',
    '봄',
    '여름',
    '가을',
    '겨울',

    // 감정 및 추상 명사
    '사랑',
    '꿈',
    '희망',
    '행복',
    '기쁨',
    '빛',
    '열정',
    '평화',
    '고요',
    '위로',
    '설렘',
    '온기',

    // 동물 관련 명사
    '고양이',
    '강아지',
    '호랑이',
    '사자',
    '곰',
    '여우',
    '펭귄',
    '토끼',
    '독수리',
    '공룡',
    '다람쥐',
    '새우',

    // 음식 및 사물 명사
    '사과',
    '딸기',
    '복숭아',
    '포도',
    '바나나',
    '초코',
    '우유',
    '커피',
    '떡',
    '빵',
    '달걀',
    '밥',
    '국',
    '책',
    '노트',
    '연필',
    '가방',
    '별빛',
    '시계',

    // 기타
    '추억',
    '행운',
    '이야기',
    '마음',
    '여행',
    '길',
    '달빛',
    '해변',
    '바위',
    '향기',
    '낮',
    '밤'
  ];

  const randomPick = (arr) => arr[Math.floor(Math.random() * arr.length)];

  let nickname = '';
  while (nickname.length < 6) {
    const 단어 = randomPick(명사목록);
    if (nickname.length + 단어.length <= 6) {
      nickname += 단어;
    }
  }

  user_name.value = nickname;
}

async function update_user_name() {
  const data = await $fetch(`/backend/user/profile/name`, {
    headers: {
      accept: 'application/json'
    },
    method: 'POST',
    body: JSON.stringify({
      token: $store.state.token,
      username: user_name.value
    })
  });

  alert('Successfully update');
}

get_user_info();
</script>

<style>
/* Optional custom styles */
</style>
