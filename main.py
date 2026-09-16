"""A simple command-line calculator."""


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero")
    return first / second


def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    print("Simple Calculator")
    print("Supported operations: +, -, *, /")

    try:
        first = float(input("First number: "))
        operator = input("Operation: ").strip()
        second = float(input("Second number: "))

        if operator not in operations:
            print("Error: unsupported operation")
            return

        result = operations[operator](first, second)
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
