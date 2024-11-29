<script>
export default {
  computed: {
    token() {
      return this.$store.state.token;
    }
  },
  methods: {
    updateToken() {
      const timestamp = Date.now();
      this.$store.commit('setToken', timestamp.toString());
    }
  }
};
</script>

<template>
  <div>
    <p>현재 토큰: {{ token }}</p>
    <button @click="updateToken">토큰 업데이트</button>
  </div>
</template>
