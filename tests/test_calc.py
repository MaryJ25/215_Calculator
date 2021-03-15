from calculator.calc import Calculator

c = Calculator()


class TestClass:
    def test_get_current(self):
        """Tests that the get_current returns correct value"""
        result = c.get_current()
        assert result == 0

    def test_start(self):
        """Tests that using start the current value is changed"""
        result = c.start(10)
        assert result == 10

    def test_add(self):
        """Tests addition"""
        c.start(10)
        result = c.add(10)
        assert result == 20

    def test_reset(self):
        """Testing reset method"""
        c.start(10)
        result = c.reset()
        assert result == 0

    def test_subtract(self):
        """Tests subtraction"""
        c.reset()
        result = c.subtract(10)
        assert result == -10

    def test_multiply(self):
        """Tests multiplication"""
        c.start(5)
        result = c.multiply(2)
        assert result == 10

    def test_divide(self):
        """Tests division"""
        c.start(10)
        result = c.divide(5)
        assert result == 2

    def test_divide_zero_current(self):
        """Tests that zero is returned if current value is zero"""
        c.reset()
        result = c.divide(10)
        assert result == 0

    def test_divide_zero_given(self):
        """Tests that zero is returned if given value is zero"""
        c.start(10)
        result = c.divide(0)
        assert result == 0

    def test_power(self):
        """Tests exponentiation"""
        c.start(4)
        result = c.power(2)
        assert result == 16

    def test_root_square(self):
        """Tests square root"""
        c.start(16)
        result = c.root(2)
        assert result == 4

    def test_root_n(self):
        """Tests nth root"""
        c.start(64)
        result = c.root(3)
        assert result == 4
