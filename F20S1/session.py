print("Hello World")

name = input("What is you name? ")

print(name*2)

# str, int, float, bool, list, dictionaries

age = input("What is you age? ")
age = int(age)
print(f"You where born {2020-age}")

if age >= 15:
    print(f"{name} you are allowed to drive a moped")
else:
    print(f"{name} you are not allowed to drive a moped")


number_of_runs = 12
i = 1
while i <= number_of_runs:
    print(i*i)
    i = i+1

print(type(name))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def born(self):
        return 2020-self.age


person = Person(name, age)

persons = [
    Person("Marcus", 32),
    Person("Erika", 30),
    Person("Goran", 64)
]
print(persons[0])
print(persons[1])

i = 0
while i < len(persons):
    print(persons[i])
    i = i+1

for p in persons:
    print(f"{p.name}, {p.age}, {p.born()}")

moped = age >= 15
print(moped)
if moped:
    print(f"{name} you are allowed to drive a moped")
else:
    print(f"{name} you are not allowed to drive a moped")

persons_dic = {
    "Marcus": Person("marcus", 32)
}
print(persons_dic["Marcus"])
