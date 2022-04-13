import requests
def web_request():
    res = requests.get("https://skaehub.com")
    print({"text": res.text})
    print("\n")
    print({"content": res.content})
    print("\n\n")
    r = requests.get('https://api.github.com/events', stream=True)
    print(r.raw)
    print(r.raw.read(15))

print(web_request())