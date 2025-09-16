num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /):").lower()

match operation:
    case "+":
        result = float(num1) + float(num2)
        print(f"The result is {result}.")
    case "-":
        result = float(num1) - float(num2)
        print(f"The result is {result}.")
    case "*":
        result = float(num1) * float(num2)
        print(f"The result is {result}.")
    case "/":
        if float(num2) == 0:
            print("Cannot divide by zero.")
        else:
            result = float(num1) / float(num2)
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")