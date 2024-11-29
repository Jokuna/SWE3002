import { createStore } from 'vuex';

export default defineNuxtPlugin((nuxtApp) => {
  const store = createStore({
    state: () => ({
      token: '', // 기본 상태
    }),
    mutations: {
      setToken(state, newToken) {
        state.token = newToken;

        // `localStorage`에 상태 저장
        localStorage.setItem('token', newToken);
      },
      clearToken(state) {
        state.token = '';

        // `localStorage`에서 상태 제거
        localStorage.removeItem('token');
      },
    },
    actions: {
      updateToken({ commit }, newToken) {
        commit('setToken', newToken);
      },
    },
    getters: {
      getToken(state) {
        return state.token;
      },
    },
  });

  // 애플리케이션 로드 시 `localStorage`에서 상태 복원
  if (process.client) {
    const savedToken = localStorage.getItem('token');
    if (savedToken) {
      store.commit('setToken', savedToken);
    }
  }

  nuxtApp.vueApp.use(store);

  return {
    provide: {
      store,
    },
  };
});
