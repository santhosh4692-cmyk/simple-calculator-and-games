# Simple command-line calculator


def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return a / b
    raise ValueError(f"unknown operator: {op}")


def main():
    print("Simple Calculator (type 'q' to quit)")
    while True:
        expr = input("\nEnter: number operator number (e.g. 12 + 7): ").strip()
        if expr.lower() == "q":
            print("Goodbye!")
            break
        parts = expr.split()
        if len(parts) != 3:
            print("Please use the format: number operator number")
            continue
        try:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
            result = calculate(a, op, b)
            print("Result:", round(result, 4))
        except (ValueError, ZeroDivisionError) as err:
            print("Error:", err)


if __name__ == "__main__":
    main()
