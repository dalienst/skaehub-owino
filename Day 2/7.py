from urllib import response
import requests
import json

def get_dict_data():
    url = "https://data.townofcary.org/api/v2/catalog/datasets/rdu-weather-history"

    response = requests.get(url).text

    dict_data = json.loads(response)
    return dict_data

print(get_dict_data())