import pytest
import yaml
from typing import List

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

# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     pass
#     # items.

def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env", 
                default="test",
                dest='env',
                help='set your run env')

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')

    if myenv == "test":
        print("读取测试数据") 
        with open('./test.yml','r') as f:
            datas = yaml.safe_load(f)
    elif myenv == "dev":
        print("读取开发数据")
        with open('./dev.yml','r') as f:
            datas = yaml.safe_load(f)
    elif myenv == "st":
        print("读取st数据")
        with open('./st.yml','r') as f:
            datas = yaml.safe_load(f)
            
    return datas