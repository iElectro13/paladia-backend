import faker
from flask import jsonify
import requests
from faker import Faker
from random import randint, choice

fake = Faker()

my_word_list = [
    'danish', 'cheesecake', 'sugar',
    'Lollipop', 'wafer', 'Gummies',
    'sesame', 'Jelly', 'beans',
    'pie', 'bar', 'Ice', 'oat']

categories = [
    "aventura",
    "infantil",
    "comic",
    "novela",
    "poesia",
    "terror"
]
url = "https://paladia-api.herokuapp.com/api/v1/books/new"

for i in range(30):
    image = requests.get('https://api.lorem.space/image/book?w=150&h=220')
    image = image.url

    data = {
        "title":fake.sentence(ext_word_list=my_word_list),
        "category":choice(categories),
        "description":fake.sentence(ext_word_list=my_word_list),
        "image":image,
        "price": randint(1,20),
        "seller":fake.name()
    }
    requests.post(url, json=data)



"""
Esquema para enviar post request:
{
    "title":"Cien años de soledad",
    "category":"Realismo magico",
    "description":"Cien años de soledad es una novela del escritor colombiano Gabriel García Márquez, ganador del Premio Nobel de Literatura en 1982.",
    "image":"no-image",
    "price": 100,
    "seller":"Enmanuel Pereira"
}
"""