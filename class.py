class Person:
    def __init__(self, name):
        Person.name =  name
    def talk(self):
        print(f"Hi, {Person.name}!")

        print("You talk so sweet.6")

person1 = Person("Riyazul Arfaat")
# print(person1.name)
person1.talk()