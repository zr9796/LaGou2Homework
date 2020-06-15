import pytest

@pytest.fixture(autouse=True, scope="module")
def login():
    print("开始计算")
    print("***I've been logged in***")
    yield ['zr9796', '123456']
    print("计算结束")

@pytest.fixture()
def login1():
    print("***I've been logged in***")
    return ['abc', '123456']

    