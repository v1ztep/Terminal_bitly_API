import requests
from dotenv import load_dotenv
import os
import json

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

def main():
    user_input = input('Введите ссылку:')
    try:
        link = shorten_link(os.getenv("TOKEN"), user_input)
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка')
        return

    print(link)

if __name__ == '__main__':
    main()
