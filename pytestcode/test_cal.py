import pytest
import yaml
from cal import Calculator

class TestCal:

    def setup(self):
        self.cal = Calculator()

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['add'])
    def test_add(self, a, b, c):
        print(f"测试 {a} + {b} = {c}")
        assert c == self.cal.add(a, b)
    
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["add"])
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['sub'])
    def test_sub(self, a, b, c):
        print(f"测试 {a} - {b} = {c}")
        assert c == self.cal.sub(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['div'])
    def test_div(self, a, b, c):
        print(f"测试 {a} / {b} = {c}")
        assert c == self.cal.div(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['mul'])
    def test_mul(self, a, b, c):
        print(f"测试 {a} * {b} = {c}")
        assert c == self.cal.mul(a, b)

