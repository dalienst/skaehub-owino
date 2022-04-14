import requests
from requests.exceptions import Timeout

url = "https://skaehub.com/"
def timeout_request(url):
    try:
        data = requests.get(url, timeout=1.0)
        return data.status_code
    except Timeout as err:
            return err

print(timeout_request(url))