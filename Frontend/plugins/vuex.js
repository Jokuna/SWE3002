import { createStore } from 'vuex';

export default defineNuxtPlugin((nuxtApp) => {
  const store = createStore({
    state: () => ({
      token: '', // 기본 상태
      filterData: {}, // 새로운 JSON 데이터 상태
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
      setFilterData(state, data) {
        state.jsonData = data;
        localStorage.setItem('filterData', JSON.stringify(data));
      },
      clearFilterData(state) {
        state.jsonData = {};
        localStorage.removeItem('filterData');
      },
    },
    actions: {
      updateToken({ commit }, newToken) {
        commit('setToken', newToken);
      },
      updateFilterData({ commit }, data) {
        commit('setFilterData', data);
      },
    },
    getters: {
      getToken(state) {
        return state.token;
      },
      getFilterData(state) {
        return state.filterData;
      },
    },
  });

  // 애플리케이션 로드 시 `localStorage`에서 상태 복원
  if (process.client) {
    const savedToken = localStorage.getItem('token');
    const savedFilterData = localStorage.getItem('filterData');

    if (savedToken) {
      store.commit('setToken', savedToken);
    }

    if (savedFilterData) {
      try {
        store.commit('filterData', JSON.parse(savedFilterData));
      } catch (error) {
        console.error('Error parsing JSON data from localStorage:', error);
      }
    }
  }

  nuxtApp.vueApp.use(store);

  return {
    provide: {
      store,
    },
  };
});
