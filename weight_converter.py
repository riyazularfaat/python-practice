weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit == "L" or unit == "l":#if unit.upper() == "L":
    weight = weight * 0.45
    print(f"You are {weight} kg")
elif unit == "K" or unit == "k":
    weight = int(weight) / 0.45
    print(f"You are {weight} pounds")