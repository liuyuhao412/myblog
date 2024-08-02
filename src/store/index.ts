import { createStore } from 'vuex';

export default createStore({
    state: {
        isLogin: false,
    },
    mutations: {
        setLogin(state, status: boolean) {
            state.isLogin = status;
        },
    },
    actions: {
        login({ commit }) {
            // 在这里可以执行登录逻辑，如调用 API
            commit('setLogin', true);

        },
        logout({ commit }) {
            commit('setLogin', false);
        },
    },
    getters: {
        isLogin: (state) => state.isLogin,
    },
});
