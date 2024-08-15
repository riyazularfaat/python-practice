def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

len = int(input('How many numbers do you want to store in the list: '))

numbers = []
for i in range(0, len):
    print('Enter number ', i+1, ': ', end = " ")
    number = int(input())
    numbers.append(number)

sum = sum_list(numbers)
print('Sum: ', sum)