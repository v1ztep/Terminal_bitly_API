import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://github.com/v1ztep"

def main():
    headers = {
        'Authorization': f'Bearer {os.getenv("TOKEN")}',
        'Content-Type': 'application/json',
    }
    data = '{"long_url": "https://github.com/v1ztep"}'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
    response.raise_for_status()

    print(response)
    print(response.text)

if __name__ == '__main__':
    main()
