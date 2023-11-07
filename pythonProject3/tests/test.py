import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_subtraction_success(self):
        assert self.calc.subtraction(self,5,5) == 0

    def test_division_success(self):
        assert self.calc.division(self, 5, 5) == 1

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def teardown(self):
        print('Выполнение метода Teardown')



