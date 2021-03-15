from calculator.calculator import Calculator

c = Calculator()

c.start(5)
print(c.add(10))
print(c.add(15))
print(c.get_current())
print(c.divide(2))
c.start(4)
print(c.multiply(4))
print(c.root(2))
