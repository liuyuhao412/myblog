import { createStore } from 'vuex';

export default createStore({
    state: {
        isLogin: JSON.parse(localStorage.getItem('isLogin') || 'false'),
    },
    mutations: {
        setLogin(state, status: boolean) {
            state.isLogin = status;
            localStorage.setItem('isLogin', JSON.stringify(status));
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
