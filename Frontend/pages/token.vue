<script setup>
import { useNuxtApp } from '#app';

const { $store } = useNuxtApp();

// Vuex 상태 접근
const token = $store.state.token;

// Vuex 상태 업데이트
function updateToken() {
  const timestamp = Date.now();
  $store.commit('setToken', timestamp.toString());
}
</script>

<template>
  <div>
    <p>현재 토큰: {{ $store.state.token }}</p>
    <button @click="updateToken">토큰 업데이트</button>
  </div>
</template>
