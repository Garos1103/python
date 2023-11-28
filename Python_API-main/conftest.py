import pytest
import yaml
import requests


with open('config.yaml') as file:
    my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username':'Garos1103', 'password': 'adgjmptw1103'})
    token = obj_data.json()['token']
    return token

@pytest.fixture()
def postP():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": my_dict['token']},data={
        'username':'Garos1103',
        'password': 'adgjmptw1103',
        'title': 'newTitle',
        'description': 'Anything',
        'content':'we will see'})
    return obj_data.json()['description']
