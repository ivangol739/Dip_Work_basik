import os
import requests
import json
from pprint import pprint
from tqdm import tqdm


class YaUploader:

    def __init__(self, token):
        self.token = token

    # Загрузка фото на ЯндексДиск
    def upload(self):
        self.apiurl = 'https://cloud-api.yandex.net/v1/disk/resources'
        directory = 'photos_vk/'
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
            response_upload = requests.get(self.apiurl + '/upload', headers=headers,
                                           params={'path': data + photo, "overwrite": "true"})
            res = response_upload.json().get("href")
            response_url = requests.put(res, data=open(directory + photo, 'rb'))
