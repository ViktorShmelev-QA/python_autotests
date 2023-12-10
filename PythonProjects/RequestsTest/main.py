import requests

response=requests.post(url='https://api.pokemonbattle.me:9104/trainers/reg',
                       json={ 
                       "trainer_token": "9a1b7abc5a427f63ff09ed68f6fd6bf8",
                       "email": "shmelev737@gmail.com",
                       "password": "89832812999K"},
                       headers={'Content-Type': 'application/json'})
print(response.text)

response=requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email',
                       json={
                       "trainer_token": "9a1b7abc5a427f63ff09ed68f6fd6bf8"},
                        headers={'Content-Type': 'application/json'})
print(response.text)

response= requests.post('https://api.pokemonbattle.me:9104/pokemons',
                        json={
                        "name":"generate",
                        "photo":"generate"},
                        headers = {"trainer_token": "9a1b7abc5a427f63ff09ed68f6fd6bf8" ,"Content-Type":"application/json"})
print(response.text)

response= requests.put('https://api.pokemonbattle.me:9104/pokemons',
                       json={
                        "pokemon_id": "21500",
                        "name":"autotesphyton_Shmel",
                        "photo":"https://dolnikov.ru/pokemons/albums/008.png" },
                        headers = {"trainer_token": "9a1b7abc5a427f63ff09ed68f6fd6bf8" ,"Content-Type":"application/json"})
print(response.text)

response= requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                        json={
                        "pokemon_id": "21500"},
                        headers = {"trainer_token": "9a1b7abc5a427f63ff09ed68f6fd6bf8" ,"Content-Type":"application/json"})
print(response.text)