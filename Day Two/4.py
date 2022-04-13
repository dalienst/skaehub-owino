import requests
url = 'https://api.github.com/events'
def web_request(url):
    try:
        res = requests.get(url)
        res_status =  res.status_code
        res_content = res.content
        res_text = res.text
        r = requests.get(url, stream=True)
        r_raw = r.raw
        return res_content, res_text,r_raw, res_status
    except requests.exceptions.RequestException as err:
            return err

print(web_request(url))