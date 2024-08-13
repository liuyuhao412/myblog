import { createStore } from 'vuex';
import instance from "@/utils/http"

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
        async login({ commit }) {
            commit('setLogin', true);
        },
        logout({ commit }) {
            commit('setLogin', false);
            localStorage.removeItem('token');
        },
        async checkAuth({ commit }) {
            const token = localStorage.getItem('token');
            if (token) {
                try {
                    const response = await instance.get('/protected_content');
                    if (response.status == 200) {
                        commit('setLogin', true);
                    } else {
                        commit('setLogin', false);
                        localStorage.removeItem('token');
                    }
                } catch (error) {
                    commit('setLogin', false);
                    localStorage.removeItem('token');
                }
            } else {
                commit('setLogin', false);
            }
        }
    },
    getters: {
        isLogin: (state) => state.isLogin,
    },
});
