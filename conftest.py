import os
import random
import pytest
from commons_qa.api.api_client import ApiClient

def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='dev', help='select AWS env')
    parser.addoption('--role', action='store', default='', help='"ci" to used role based auth')

def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["role"] = config.getoption('role')

def random_int_generator(lenght):
    min_value = pow(10, lenght - 1)
    max_value = pow(10, lenght) - 1
    return random.randint(min_value, max_value)

@pytest.fixture()
def create_random_user_data_conftest():
    api_client = ApiClient('https://2p5mwal37l.execute-api.us-east-1.amazonaws.com/v1/contacts')
    random = str(random_int_generator(8))
    payload = {
        "id": random,
        "firstname": "santi",
        "lastname": "amorin"
    }
    response = api_client.post(payload=payload)
    print(response.json())
    yield response