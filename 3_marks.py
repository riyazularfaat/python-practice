eng = int(input("Enter mark of English: "))
math = int(input("Enter mark of Math: "))
che = int(input("Enter mark of Chemistry: "))
phy = int(input("Enter mark of Physics: "))
bio = int(input("Enter mark of Biology: "))

totalMarks = eng + math + che + phy + bio
percentage = (totalMarks/500) * 100

print("English = ", eng)
print("Math = ", math)
print("Chemistry = ", che)
print("Physics = ", phy)
print("Biology = ", bio)
print("Total marks = ", totalMarks)
print("Percentage = ", percentage)