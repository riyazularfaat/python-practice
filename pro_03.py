num1 = int(input('Enter divident: '))
num2 = int(input('Enter divisor '))

try:
    result = num1 / num2
    print(int(result))
except ZeroDivisionError:
    print("Cannot be divided by zero.")

