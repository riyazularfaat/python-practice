def calculator():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    opt = input("Enter the operator: ")
    
    try:
        if opt == '+':
            result = num1 + num2
        
        elif opt == '-':
            result = num1 - num2
        
        elif opt == '*':
            result = num1 * num2
        elif opt == '/':
            result = num1 / num2
        elif opt == '^':
            result = num1 ** num2
        else:
            print("Invalid operator.")
    
        print(result)
    
    except DataTypeError:
        print("Please enter only numbers")
    except ZeroDivisionError:
        print("Cannot divided by zero")
    
        


calculator()
    