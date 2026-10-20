
def calculator():
    print("=== Python Calculator ===")
    print("Welcome to my first GitHub project!")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = a + b
            elif choice == "2":
                result = a - b
            elif choice == "3":
                result = a * b
            else:
                if b == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = a / b

            print(f"Result: {result}")

        except ValueError:
            print("Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
