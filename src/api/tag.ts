import instance from "@/utils/http"


export const get_tags = (username: string, password: string) => {
    return instance.post('/login', { username, password });
};