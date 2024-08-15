n = int(input("Enter the number of elements: "))
numbers = []
for i in range(0, n):
    num = int(input())
    numbers.append(num)
unique = []
duplicate = []

for num in numbers:
    if num not in unique:
        unique.append(num)
    else:
        duplicate.append(num)
print("Numbers without duplicate: ",unique)
print("Duplicates: ",duplicate)