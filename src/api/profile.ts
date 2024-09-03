import instance from "@/utils/http"


export const get_user_profile = () => {
    return instance.get('/get-user-profile')
};

export const upload_avatar = (file: any) => {
    const formData = new FormData();
    formData.append('file', file);

    return instance.post('/upload-avatar', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
};

export const update_profile = (username: string, name: string, email: string, avatar: string, info: string) => {
    return instance.post('/update-profile', { username, name, email, avatar, info });
};
