import pytest
from cal import Calculator


def setup_module():
    print("开始计算")
    
def teardown_module():
    print("计算结束")

class TestCal:

    def setup(self):
        self.cal = Calculator()

    def test_add(self):
        assert 3 == self.cal.add(1, 2)
    
    def test_add1(self):
        assert 300 == self.cal.add(100, 200)
    
    def test_add2(self):
        assert 6.6 == self.cal.add(2.72, 3.88)
    
    def test_sub(self):
        assert 1 == self.cal.sub(3, 2)
    
    def test_sub1(self):
        assert 100 == self.cal.sub(300, 200)
    
    def test_sub2(self):
        assert 3.38 == self.cal.sub(6.5, 3.12)
    
    def test_mul(self):
        assert 6 == self.cal.mul(2, 3)
    
    def test_mul1(self):
        assert 600 == self.cal.mul(20, 30)
    
    def test_mul2(self):
        assert 700 == self.cal.mul(200, 3.5)
    
    def test_div(self):
        assert 1 == self.cal.div(1, 1)
    
    def test_div1(self):
        assert 20 == self.cal.div(60, 3)
    
    def test_div2(self):
        assert 5 == self.cal.div(6, 1.2)
        