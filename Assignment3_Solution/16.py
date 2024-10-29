def basic_calculator():
    
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        
        operation = input("Enter an operation (+, -, *, /): ")
        
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")
            return
        
        
        print(f"The result of {num1} {operation} {num2} is: {result}")
    
    


basic_calculator()
