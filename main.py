import requests
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description='Скрипт сокращает ссылки и показывает количество переходов (за все дни) через сервис bitly.com.'
    )
    parser.add_argument('link', help='Ссылка')
    return parser.parse_args()


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
    return f'{parsed.netloc}{parsed.path}'


def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{strip_scheme(url)}',
                            headers=headers)
    return response.ok


def main():
    load_dotenv()
    args = get_args()

    user_input = args.link
    token = os.getenv("BITLY_TOKEN")

    try:
        if is_bitlink(token, user_input):
            clicks_amount = count_clicks(token, user_input)
            print(f'По вашей ссылке прошли {clicks_amount} раз(а)')
        else:
            link = shorten_link(token, user_input)
            print(f'Короткая ссылка: {link}')
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка')


if __name__ == '__main__':
    main()
