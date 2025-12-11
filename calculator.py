def menu():
    print("Welcome to the calculator program. ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")

try:
    while True:
        menu()
        print("=" * 50)

        ch = int(input("Enter your choice: "))
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        try:
            match ch:
                case 1:
                    print(f"Addition of {a} and {b} is {a+b}")
                case 2:
                    print(f"Subtraction of {a} and {b} is {a-b}")    
                case 3:
                    print(f"Multiplication of {a} and {b} is {a*b}")
                case 4:
                    print(f"Division of {a} and {b} is {a/b}")
                case 5:
                    print(f"Floor Division of {a} and {b} is {a//b}")
                case 6:
                    print(f"Modulus of {a} and {b} is {a%b}")
                case 7:
                    print(f"Exponentiation of {a} and {b} is {a**b}")
                case _:
                    print("Invalid choice, please try again")
        except ZeroDivisionError:
            print(" Error: Division by zero is not allowed!")

        dc = input("Do you want some more calculation (yes/no): ")
        if dc.lower() == "no":
            print("Thanks for using this Project!")
            break  

except ValueError:
    print("Don't enter alphabets or strings where numbers are required!")