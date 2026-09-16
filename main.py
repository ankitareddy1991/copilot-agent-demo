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


def is_numeric(value):
    """Return True when value can be converted to a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    print("Simple Calculator")
    print("Supported operations: +, -, *, /")

    first_input = input("First number: ").strip()
    if not is_numeric(first_input):
        print("Error: first input must be numeric")
        return

    operator = input("Operation: ").strip()
    second_input = input("Second number: ").strip()
    if not is_numeric(second_input):
        print("Error: second input must be numeric")
        return

    try:
        first = float(first_input)
        second = float(second_input)

        if operator not in operations:
            print("Error: unsupported operation")
            return

        result = operations[operator](first, second)
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
