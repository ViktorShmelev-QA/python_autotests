import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response=requests.get(f'{HOST}/trainers', params={'trainer_id':3839})
    assert response.status_code == 200
    assert response.json()['trainer_name'] =='VIKTOR'