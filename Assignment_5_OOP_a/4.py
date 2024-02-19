class Calculator(object):
    def add(self, num1, num2):
        print(num1+num2)

    def subtract(self, num1, num2):
        print(num1-num2)

    def multiply(self, num1, num2):
        print(num1*num2)

    def divide(self, num1, num2):
        print(num1//num2)


calculator = Calculator()
calculator.add(10, 5)
calculator.subtract(10, 5)
calculator.multiply(10, 5)
calculator.divide(10, 5)