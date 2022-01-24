# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json

user = 'Alex-from-belgorod'
url = f'https://api.github.com/users/{user}/repos'
r = requests.get(url).json()

with open('responce.json', 'w', encoding='utf-8') as f:
    json.dump(r, f, indent=4)

