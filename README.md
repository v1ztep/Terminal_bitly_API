# Сокращение ссылок bit.ly

Скрипт сокращает ссылки и показывает количество переходов (за все дни) через сервис [bitly.com](https://app.bitly.com/).
Можно ввести длинную ссылку и получить битлинк и кол-во переходов по ней, либо передать битлинк и получить только количество переходов.

## Настройки

Необходимо зарегистрироваться на сайте [bitly.com](https://bitly.com/a/sign_up) и получить [ключ к API Bitly](https://bitly.com/a/oauth_apps) `GENERIC ACCESS TOKEN`.
Затем создать файл `.env` в корневой папке с кодом и записать туда ключ в формате `TOKEN=ВАШ КЛЮЧ`

## Запуск

Для запуска библиотеки у вас уже должен быть установлен [Python 3](https://www.python.org/downloads/release/python-379/).

- Скачайте код.
- Установите зависимости командой `pip install -r requirements.txt`.
- Запустите скрипт командой `python main.py`.


