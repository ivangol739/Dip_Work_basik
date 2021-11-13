from ClassVK import user_VK
from YaUploader import YaUploader

if __name__ == '__main__':
    # Получение токена и запуск модуля ВК
    # with open('token.txt', encoding='utf-8') as f:
    #     TOKEN_VK = f.readline().strip()
    TOKEN_VK = ''
    id_user = ''
    get_photo_vk = user_VK(TOKEN_VK, id_user)
    photo_vk = get_photo_vk.get_photos()

    #Получение токена и запуск модуля Яндекс
    # with open('token_y.txt', encoding='utf-8') as f:
    #     TOKEN_YA = f.readline().strip()
    TOKEN_YA = ''
    uploader = YaUploader(TOKEN_YA)
    uploader.upload()






