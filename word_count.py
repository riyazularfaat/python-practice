text = input("Enter text: ")
count = 0


for char in text:
    if char == " ":
        count += 1
count += 1
print(count)