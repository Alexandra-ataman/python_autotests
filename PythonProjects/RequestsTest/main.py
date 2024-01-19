"""
Api tests for pokemons
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': '489e48a2ae71da2b5fc1854332f16a48'}

# Создание покемона
body = {
    "name": "generate",
    "photo": "generate"
}

# Создание покемона
response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body)

if response_create.status_code == 201:
    created_pokemon_id = response_create.json().get('id')

    # Обновление имени покемона
    new_name = "Pokemon"
    response_update = requests.patch(url=f'{URL}/pokemons', headers=HEADER, json={"pokemon_id": created_pokemon_id, "name": new_name})

    print(f'Статус код создания: {response_create.status_code}. Сообщение: {response_create.json()}')
    print(f'Статус код обновления имени: {response_update.status_code}. Сообщение: {response_update.json()}')

    # Попытка поймать покемона в покебол
    response_capture = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json={"pokemon_id": created_pokemon_id})
    
    print(f'Статус код попытки поймать покемона: {response_capture.status_code}. Сообщение: {response_capture.json()}')
else:
    print(f'Ошибка создания покемона. Статус код: {response_create.status_code}. Сообщение: {response_create.json()}')