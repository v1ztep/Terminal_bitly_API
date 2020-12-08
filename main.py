import requests
from dotenv import load_dotenv
import os
from urllib.parse import urlparse


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {"long_url": url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             headers=headers, json=data)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink

def count_clicks(token, bitlink):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{strip_scheme(bitlink)}/clicks/summary',
                            headers=headers)
    response.raise_for_status()

    total_clicks = response.json()["total_clicks"]
    return total_clicks

def strip_scheme(url):
    parsed = urlparse(url)
    return parsed.netloc + parsed.path

def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    try:
        response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{strip_scheme(url)}',
                                headers=headers)
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError:
        return False


def main():
    load_dotenv()

    user_input = input('Введите ссылку: ')
    token = os.getenv("BITLY_TOKEN")

    if is_bitlink(token, user_input):
        try:
            clicks_amount = count_clicks(token, user_input)
            print(f'По вашей ссылке прошли {clicks_amount} раз(а)')
        except requests.exceptions.HTTPError:
            print('Неправильная ссылка')
            return
    else:
        try:
            link = shorten_link(token, user_input)
            print(f'Короткая ссылка: {link}')
        except requests.exceptions.HTTPError:
            print('Неправильная ссылка')
            return


if __name__ == '__main__':
    main()
