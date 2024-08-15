size = int(input('Enter the number of elements: '))


"""
sum=0
i = 1
while i <= size:
    number = float(input())
    sum += number
    i += 1"""

numbers =[]
for i in range(0, size):
    number = int(input('> ' ))
    numbers.append(number)

total = sum(numbers)
average = total/size
print('Average: ', average)