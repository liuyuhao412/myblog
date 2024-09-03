import instance from "@/utils/http"


export const createArticle = (title: string, content: string) => {
    return instance.post('/articles', { title, content });
};

export const getArticles = () => {
    return instance.get('/articles');
};

export const getArticle = (id: number) => {
    return instance.get(`/articles/${id}`);
};

export const editArticle = (id: number, title: string, content: string) => {
    return instance.put(`/articles/${id}`, { title, content });
};

export const delArticle = (id: number) => {
    return instance.delete(`/articles/${id}`);
};
