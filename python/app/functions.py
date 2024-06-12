def hello_world():
    print("Hello, world!")


def add(x: float, y: float):
    return x + y


def divide(x: float, y: float):
    return x / y


def main():
    hello_world()
    try:
        print("\nEnter two numbers:")
        x, y = float(input("> ")), float(input("> "))
        print(f"{x} + {y} = {add(x, y)}")
        print(f"{x} / {y} = {divide(x, y)}")
    except ValueError as err:
        print(f"Error: {err}\n")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
