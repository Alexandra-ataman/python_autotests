import requests
import pytest


URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': '489e48a2ae71da2b5fc1854332f16a48'}

# KTI-1. запрос GET /trainers - в ответе статус код 200
def test_get_trainers():
    response = requests.get(url=f'{URL}/trainers', timeout=3)
    assert response.status_code == 200, 'Unexpected status code'

# KTI-2. в ответе приходит строчка с именем тренера "Александра"
def test_get_trainers_by_name():
    response = requests.get(url=f'{URL}/trainers', params= {'trainer_id': 3481}, timeout=3)
    assert response.json()['trainer_name'] == 'Alexandra'