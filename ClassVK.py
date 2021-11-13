import os
import requests
import json
from pprint import pprint
from tqdm import tqdm


class user_VK:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, vk_id):
        self.token = token
        self.id_user = vk_id

        method = 'users.get'
        self.params = {
            'user_ids': self.id_user,
            'access_token': self.token,
            'v': '5.131'
        }
        # user_info = requests.get(self.url + method, params=self.params)
        # self.user_id = user_info.json()['response'][0]['id']
        # user_first_name = user_info.json()['response'][0]['first_name']
        # user_last_name = user_info.json()['response'][0]['last_name']
        # self.user_name = f'{self.user_id} {user_first_name} {user_last_name}'

    def get_photos(self):
        # Получение фото с VK
        method = 'photos.get'
        directory = 'photos_vk/'
        photos_get_params = {
            'album_id': 'profile',
            'extended': '1'
        }
        req = requests.get(self.url + method,
                           params={**self.params, **photos_get_params}).json()

        photos_list = []
        for photo in req['response']['items']:
            photos_dict = {}
            if photo['likes']['count'] not in photos_dict:
                photos_dict['file_name'] = str(photo['likes']['count']) + ".jpg"
            max_photo = photo['sizes'][-1]
            photos_dict['size'] = max_photo['type']
            photos_list.append(photos_dict)
            img = requests.get(max_photo['url']).content
            with open(directory + photos_dict['file_name'], 'wb') as file:
                file.write(img)

        # Информация по фотографиям в json файле
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(photos_list, file)
