try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(risk)
except ValueError:
    print("Invalid value\nEnter a valid number.....")
except ZeroDivisionError:
    print("Age cannot be zero")