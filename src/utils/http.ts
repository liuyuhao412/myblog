import axios, { AxiosInstance, AxiosResponse } from 'axios';

const instance: AxiosInstance = axios.create({
    baseURL: "http://127.0.0.1:5000", // 你的 API 基础 URL
    timeout: 10000, // 请求超时时间
    headers: {
        'Content-Type': 'application/json',
        // 你可以在这里添加其他的默认请求头
    },
});

instance.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;

        }
        return config;
    },
    (error) => {
        // 处理请求错误
        return Promise.reject(error);
    }
);

instance.interceptors.response.use(
    (response: AxiosResponse) => {
        return response

    },
    (error) => {
        // 处理响应错误
        return Promise.reject(error);
    }
);

export default instance;