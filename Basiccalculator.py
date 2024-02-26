import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ArithmeticError("Division by zero is not allowed.")
        return a / b

class BasicCalculator:
    def main(self):
        calc = Calculator()

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("Enter your choice (1-4): ")
        choice = int(input())

        result = None

        if choice == 1:
            result = calc.add(num1, num2)
        elif choice == 2:
            result = calc.subtract(num1, num2)
        elif choice == 3:
            result = calc.multiply(num1, num2)
        elif choice == 4:
            try:
                result = calc.divide(num1, num2)
            except ArithmeticError as e:
                print(e)
        else:
            print("Invalid choice.")

        if result is not None:
            print("Result: ", result)

if __name__ == "__main__":
    BasicCalculator().main()
