import os
import random
import pytest

def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='dev', help='select AWS env')
    parser.addoption('--role', action='store', default='', help='"ci" to used role based auth')

def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["role"] = config.getoption('role')