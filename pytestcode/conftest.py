import pytest

@pytest.fixture(autouse=True, scope="module")
def login():
    print("***I've been logged in***")
    return ['zr9796', '970906']

@pytest.fixture()
def login1():
    print("***I've been logged in***")
    return ['abc', '123456']