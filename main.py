import json
import requests
from time import sleep
from faker import Faker
import random

url = "https://api.hopysplit.com.br/v1/card-token?publicKey=pk_live_VXE0Rf7DCHUcp79xNSlKNDF1LP19ax"

def do_request():
    while True:
        nomes = [
            "Joao", "Maria", "Pedro", "Ana", "Luiz", "Carla", "Jose", "Mariana", "Fernando", "Isabela",
            "Gustavo", "Camila", "Rafael", "Juliana", "Andre", "Laura", "Lucas", "Patricia", "Marcos", "Leticia"]

        sobrenomes = [
            "Silva", "Santos", "Oliveira", "Pereira", "Ferreira", "Alves", "Souza", "Rodrigues", "Costa", "Carvalho",
            "Gomes", "Martins", "Lima", "Araujo", "Fernandes", "Barbosa", "Ribeiro", "Melo", "Pinto", "Nascimento"
        ]

        alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        fake = Faker()
        data = {
            'cvv': f'{random.randint(100, 999)}',
            'expirationMonth': random.randint(1, 12),
            'expirationYear': random.randint(2024, 2026),
            'holderName': f'{nomes[random.randint(1, 19)]} {alfabeto[random.randint(1, 25)]} {alfabeto[random.randint(1, 25)]} {sobrenomes[random.randint(1, 19)]}',
            'number': f'{fake.credit_card_number(card_type=None)}'
        }

        data_json = json.dumps(data)
        response = requests.post(url, data=data_json, headers={'Content-Type': 'application/json'})
        print(response)
        print(data_json)
        sleep(5)




do_request()
