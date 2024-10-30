import requests
import json

from django.shortcuts import render


def getlist(url):
    response1 = requests.get(url)
    print(f'ping status code: {response1.status_code}')
    print(f'ping body: {response1.text}')
    return response1.json()

def getbyID(url):
    response2 = requests.get(url)
    print(f'ping status code: {response2.status_code}')
    print(f'ping body: {response2.text}')

def create(url,data):
    headers = {'Content-Type': 'application/json'}
    response3 = requests.post(url=url, headers=headers, data=json.dumps(data))
    response_json = response3.json()
    print(f'ping status code: {response3.status_code}')
    print(f'response json: {type(response_json)} {response_json}')
    print(f'ping body: {response3.text}')

def delete(url):
    response4 = requests.delete(url)
    print(f'ping status code: {response4.status_code}')

def update(url,data):
    headers = {'Content-Type': 'application/json'}
    response5 = requests.put(url=url, headers=headers, data=json.dumps(data))
    print(f'ping status code: {response5.status_code}')
    print(f'ping body: {response5.text}')



getlist('http://127.0.0.1:1111/api/authors/')

# getbyID('http://127.0.0.1:1111/api/authors/1/')
#
# create('http://127.0.0.1:1111/api/authors/',{
#             'first_name': 'Михайло',
#             'last_name': 'Коцюбинський',
#             'birth_year': '1960',
#             'death_year': '2023',
#         })
# update('http://127.0.0.1:1111/api/authors/3/',{
#             'first_name': 'Михайло',
#             'last_name': 'Коцюбинський',
#             'birth_year': '1960',
#             'death_year': '2000',
#         })
delete('http://127.0.0.1:1111/api/authors/3/')


