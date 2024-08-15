num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))
num3 = float(input('Enter number 3: '))

"""if num1 > num2:
    large = num1
else:
    large = num2
    
if large > num3:
    largest = large
else:
    largest = num3"""

largest = max(num1, num2, num3)

print('Largest number:', int(largest))