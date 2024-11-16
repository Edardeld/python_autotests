import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '76d197614f82b260c48a998fc4d1e758'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN,
}
TRAINER_ID = '7380'
TRAINER_NAME = 'Edardeld'

# Проверяем статус 200 и наличие нужного никнейма в ответе
def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    assert TRAINER_NAME in response.text