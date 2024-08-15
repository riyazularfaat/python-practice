num = int(input("Enter list size: "))
items =[]
unique = []

for i in range(0, num):
    item = input()
    items.append(item)
    
    
def remove_duplicate(items):
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

print(remove_duplicate(items))