from urllib import response
import requests
import json

def get_dict_data(url):
        response = requests.get(url)
        data = response.json()
        return data