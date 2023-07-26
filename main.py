# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Person:
    person_count = 0

    def __init__(self,name,father_name,age):
        self.name = name
        self.father_name = father_name
        self.age = age
        Person.person_count+=1

    def __str__(self):
        return f"Name: {self.name} FatherName: {self.father_name} Age: {self.age} Person Count: {Person.person_count}"

    def __repr__(self):
        return f"Name: {self.name} FatherName: {self.father_name} Age: {self.age}"

    def __del__(self):
        self.person_count -= 1

person1 = Person("Usman","Arshad",20)
print(person1)
del person1
person2=Person("Ali","Arshad",22)
print(person2)



