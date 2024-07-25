def great_user(name):
    print(f"Hi, {name}!")
    print("Welcome to the board")
print("Start")
great_user("Arfaat")
print("Finish")

# User input
def great_user(first_name, last_name):
    print(f"Hi, {first_name} {last_name}!")
    print("Welcome to the board")
print("\nUser input start..........")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
great_user(first_name, last_name)
print("Finish")

# Keyword argument
def great_user(first, last):
    print(f"Hi, {first} {last}!")
    print("Welcome to the board")
print("\nUser input start..........")
great_user(last="Arfaat", first = "Riyazul")
print("Finish")