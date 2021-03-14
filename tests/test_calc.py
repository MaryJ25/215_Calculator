from calculator.calc import Calculator
import pytest

c = Calculator()


class TestClass:
    def test_add_one(self):
        """
        Tests addition with one parameter
        """
        result = c.add(10)
        assert result == 10

    def test_add_two(self):
        """
        Tests addition with two parameters
        """
        result = c.add(10, 2)
        assert result == 12

    def test_subtract_one(self):
        """
        Tests subtraction with one parameter
        """
        result = c.subtract(10)
        assert result == 10

    def test_subtract_two(self):
        """
        Tests subtraction with two parameters
        """
        result = c.subtract(10, 2)
        assert result == 8

    def test_multiply_one(self):
        """
        Tests multiplication with one parameter
        """
        result = c.multiply(10)
        assert result == 0

    def test_multiply_two(self):
        """
        Tests multiplication with two parameters
        """
        result = c.multiply(10, 2)
        assert result == 20

    def test_divide_one(self):
        """
        Raises an error when only one parameter given
        """
        with pytest.raises(ZeroDivisionError):
            c.divide(10)

    def test_divide_two(self):
        """
        Tests division with two parameters
        """
        result = c.divide(10, 2)
        assert result == 5

    def test_power_one(self):
        """
        Tests rising to the power with one parameter
        """
        result = c.power(10)
        assert result == 1

    def test_power_two(self):
        """
        Tests rising to the power with two parameters
        """
        result = c.power(2, 3)
        assert result == 8

    def test_root_one(self):
        """
        Tests square root
        """
        result = c.root(16)
        assert result == 4

    def test_root_two(self):
        """
        Tests root with two parameters
        """
        result = c.root(64, 3)
        assert result == 4
