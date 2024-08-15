def sum_of_digit(num):
     sum = 0
     while (num>0):
        last_digit = num % 10
        sum += last_digit
        num //= 10
     return sum

num = int(input('Enter your number: '))
sum = sum_of_digit(num)

"""
num = input('Enter your number: ')
sum = 0
for char in num:
    sum += int(char)
"""
    
print('Sum of digits: ', sum)