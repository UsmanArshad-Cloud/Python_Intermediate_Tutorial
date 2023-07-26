class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        return "Animal speaks"

class Bird(Animal):
    pass

class Parrot(Bird):
    pass

parrot = Parrot("Parrot species")
print(parrot.species)  # Output: Parrot species
print(parrot.speak())  # Output: Parrot says 'Hello!'
