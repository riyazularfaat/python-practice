n = int(input("Enter the numbers of elements: "))

numbers = []
for i in range(0, n):
    num = int(input())
    numbers.append(num)
print("Numbers = ",numbers)

max = numbers[0]
for number in numbers:
   if number > max:
       max = number
   
print("Maximum number = ", max)