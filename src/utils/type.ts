export interface LoginUser {
    username: string;
    password: string;
}

export interface RegisterUser {
    username: string;
    password: string;
    confirmPassword: string;
}

export interface UserInfo {
    username: string;
    avatar: string;
    email: string;
    info: string;
    articleCount: number;
    tagCount: number;
}

export interface ContentItem {
    id: number;
    title: string;
}

export interface CategoryItem{
    id: number;
    name: string;
    articleCount: number;
}
