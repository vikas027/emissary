import pytest

def pytest_addoption(parser):
    parser.addoption("--letter-range", action="store", default="all", choices=["ah","ip","qz","all"])


letter_range = None
def pytest_configure(config):
    global letter_range
    letter_range = config.getoption('--letter-range')
