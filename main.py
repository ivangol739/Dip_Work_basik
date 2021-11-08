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
        method = 'photos.get'
        photos_get_params = {
            'album_id': 'profile',
            'extended': '1'
        }
        req = requests.get(self.url + method, params={**self.params, **photos_get_params}).json()

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
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(photos_list, file)

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self):
        self.apiurl = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }
        params = {
            "path": directory,
            "overwrite": "true"
        }
        requests.put(self.apiurl, headers=headers, params=params)
        files_list = os.listdir(directory)
        data = os.path.join(directory)
        for photo in tqdm(files_list):
            response_upload = requests.get(self.apiurl + '/upload', headers=headers, params={'path': data + photo, "overwrite": "true"})
            res = response_upload.json().get("href")
            response_url = requests.put(res, data=open(directory + photo, 'rb'))

if __name__ == '__main__':
    with open('token.txt', encoding='utf-8') as f:
        TOKEN_VK = f.readline().strip()
    id_user = 'ivangol739'
    directory = 'photos_vk/'
    get_photo_vk = user_VK(TOKEN_VK, id_user)
    photo_vk = get_photo_vk.get_photos()

    with open('token_y.txt', encoding='utf-8') as f:
        TOKEN_YA = f.readline().strip()
    uploader = YaUploader(TOKEN_YA)
    uploader.upload()






