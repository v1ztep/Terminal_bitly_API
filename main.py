import requests
from dotenv import load_dotenv
import os
import json
from urllib.parse import urlparse

load_dotenv()

URL = "https://github.com/v1ztep"

def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {"long_url": f"{url}"}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             headers=headers, json=data)
    response.raise_for_status()
    bitlink = json.loads(response.text.replace("'",'"'))["link"]
    return bitlink

def count_clicks(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {"long_url": f"{url}"}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             headers=headers, json=data)
    response.raise_for_status()
    bitlink = json.loads(response.text.replace("'", '"'))["link"]

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{strip_scheme(bitlink)}/clicks/summary',
                            headers=headers)
    response.raise_for_status()

    total_clicks = json.loads(response.text.replace("'",'"'))["total_clicks"]
    return total_clicks

def strip_scheme(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)


def main():
    # user_input = input('Введите ссылку:')
    user_input = URL
    token = os.getenv("TOKEN")
    try:
        link = shorten_link(token, user_input)
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка')
        return
    
    try:
        clicks_amount = count_clicks(token, user_input)
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка')
        return

    print(link)
    print(clicks_amount)

if __name__ == '__main__':
    main()
