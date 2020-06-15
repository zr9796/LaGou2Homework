import pytest
import yaml
from cal import Calculator


class TestCal:
    
    def setup(self):
        self.cal = Calculator()

    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['add'])
    def test_add(self, a, b, c):
        print(f"测试 {a} + {b} = {c}")
        assert c == self.cal.add(a, b)
    
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['sub'])
    def test_sub(self, a, b, c):
        print(f"测试 {a} - {b} = {c}")
        assert c == self.cal.sub(a, b)
    
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['mul'])
    def test_mul(self, a, b, c):
        print(f"测试 {a} * {b} = {c}")
        assert c == self.cal.mul(a, b)

    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['div'])
    def test_div(self, a, b, c):
        print(f"测试 {a} / {b} = {c}")
        assert c == self.cal.div(a, b)
