import instance from "@/utils/http"


export const loginUser = (username: string, password: string) => {
    return instance.post('/login', { username, password });
};

export const registerUser = (username: string, password: string, confirmPassword: string) => {
    return instance.post('/register', { username, password, confirmPassword });
};

export const exitBlog = () => {
    return instance.post('/logout');
};



