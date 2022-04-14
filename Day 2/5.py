import requests
from requests.exceptions import Timeout

def timeout_request(url, timeout=1):
        try:
            response = requests.get(url, timeout=timeout)
            return response
        except Timeout as err:
                raise(err)