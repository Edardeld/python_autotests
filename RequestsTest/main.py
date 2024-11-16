import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '76d197614f82b260c48a998fc4d1e758'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}
body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}
body_change_pokemon = {
    "pokemon_id": "69734",
    "name": "generate",
    "photo_id": -1
}
body_catch_pokemon = {
    "pokemon_id": "135074"
}

# Создание нового покемона
response = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response.status_code)
print(response.json())

# Смена имени покемона
response = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_change_pokemon)
print(response.status_code)
print(response.json())

# Поймать покемона в покебол
response = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pokemon)
print(response.status_code)
print(response.json())




