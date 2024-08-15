num =int(input('Enter the number: '))

numbers = []
for i in range(0, num):
    if i % 3 == 0 and i % 5 ==0:
        numbers.append(i)
        

print('Numbers are: ', numbers)
        