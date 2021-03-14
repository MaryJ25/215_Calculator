class Calculator:
    @staticmethod
    def add(a=0, b=0):
        return a + b

    @staticmethod
    def subtract(a=0, b=0):
        return a - b

    @staticmethod
    def multiply(a=0, b=0):
        return a * b

    @staticmethod
    def divide(a=0, b=0):
        return a / b

    @staticmethod
    def power(a=0, b=0):
        return a ** b

    @staticmethod
    def root(a=0, b=2):
        return round(a**(1/b))
