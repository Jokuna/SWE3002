<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-white">
    <!-- Header -->
    <h1 class="text-4xl font-bold text-gray-800 mb-4">SKKU-Dormie</h1>
    <p class="text-base font-bold text-gray-800 mb-4">for find dormate</p>

    <!-- Sign Up Form -->
    <div class="w-full max-w-md bg-white p-6">
      <h2 class="text-xl font-semibold text-gray-800 mb-4">Sign up</h2>

      <form class="space-y-4" @submit.prevent="register">
        <!-- Email Number Input -->
        <div>
          <!-- <label for="email" class="block text-sm font-medium text-gray-700">
            Email Address
          </label> -->
          <div class="mt-1 relative">
            <input
              id="email"
              type="email"
              v-model="email"
              placeholder="Email Address"
              class="w-full border border-gray-300 p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
        </div>

        <!-- Verification Code -->
        <div>
          <!-- <label
            for="verification"
            class="block text-sm font-medium text-gray-700"
          >
            Verification Code
          </label> -->
          <div class="mt-1 flex">
            <input
              id="verification"
              type="text"
              placeholder="Verification Code"
              v-model="password"
              class="flex-1 border border-gray-300 p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="button"
              @click="genKey"
              class="bg-blue-500 text-white px-3 py-2 text-sm hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Get Code
            </button>
          </div>
        </div>

        <!-- Sign Up Button -->
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 text-sm font-medium hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Sign up
        </button>
      </form>

      <!-- Footer -->
      <div class="text-center mt-6">
        <a
          href="/login"
          class="text-sm text-gray-500 hover:text-blue-500 hover:underline"
        >
          I have account
        </a>
      </div>

      <div class="flex justify-center mt-6">
        <img src="/skku_logo.jpg" alt="SKKU Logo" class="h-32" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useNuxtApp } from '#app';

const { $store } = useNuxtApp();

const email = ref('');
const password = ref('');

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

  return nickname;
}

const register = async () => {
  if (!email.value) {
    alert('Please re-enter your Email.');
    return;
  }

  if (!password.value) {
    alert('Please re-enter your passkey.');
  }

  try {
    const data = await $fetch('/backend/user/register', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: {
        email: email.value,
        passkey: password.value,
        username: generateRandomNickname(),
        isMale: true,
        dormitory: -1,
        latestGPA: -1,
        isSmoke: true,
        sleepingTime: 'string',
        wakeTime: 'string',
        age: -1,
        semester: -1,
        major: 'string',
        selfIntroduction: 'string',
        trait: ['string'],
        weekendProportion: 0,
        isOpenAge: true,
        isOpenMajor: true
      }
    });

    // console.log(data);

    alert('Registration is complete. Moving to the login page.');
    await navigateTo('/login');
  } catch (error) {
    if (error.response && error.response.status === 401) {
      alert('Login failed. Please check your email and passkey.');
    } else {
      alert('An unexpected error occurred. Please try again later.');
    }
  }
};

const genKey = async () => {
  if (!email.value) {
    alert('Please re-enter your Email.');
    return;
  }

  const data = await $fetch('/backend/user/genToken', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    },
    body: {
      email: email.value
    }
  });

  alert(data.msg);
};
</script>

<style>
/* Optional custom styles */
</style>
