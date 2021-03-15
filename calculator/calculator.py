class Calculator:
    def __init__(self):
        """Initialises the class, sets to zero at the beginning"""
        self.current = 0

    def reset(self):
        """Allows to reset the calculator back to 0"""
        self.current = 0
        return self.current

    def start(self, num):
        """Allows to change the current number stored"""
        self.current = num
        return self.current

    def get_current(self):
        return self.current

    def add(self, num):
        """Addition method"""
        self.current += num
        return self.current

    def subtract(self, num):
        """Subtraction method"""
        self.current -= num
        return self.current

    def multiply(self, num):
        """Multiplication method"""
        self.current *= num
        return self.current

    def divide(self, num):
        """Division method"""
        if self.current == 0 or num == 0:
            self.current = 0
        else:
            self.current /= num
        return self.current

    def power(self, num):
        """Exponentiation method"""
        self.current **= num
        return self.current

    def root(self, num):
        """ nth root method"""
        self.current **= (1 / num)
        self.current = round(self.current)
        return self.current
