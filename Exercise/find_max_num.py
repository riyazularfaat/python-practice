import utilis as u

n = int(input("Enter the numbers of elements: "))
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
print("Numbers = ",numbers)
u.find_max(numbers)