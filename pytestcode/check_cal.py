import pytest
import yaml
from cal import Calculator


class CheckCal:
    
    def setup(self):
        self.cal = Calculator()
    
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('./data.yml', 'r'))['mod'])
    def check_mod(self, a, b, c):
        print(f"测试 {a} % {b} = {c}")
        assert c == self.cal.mod(a, b)