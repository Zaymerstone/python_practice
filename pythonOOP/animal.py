class Person:
    def __init__(self, name, age, country): # every person has a name age country and it differs for everybody
        self.name = name
        self.age = age
        self.country = country
    def tellAboutSelf(self): # method tellAboutSelf
        print(f"I am {self.name} {self.age} years old and from {self.country}")

    def drinkAlcohol(self):
        if self.age > 17:
            print(f"{self.name} is allowed to drink alcohol")
        else:
            print(f"{self.name} is too young for drinking alcohol!")

    
egor = Person("Egor", 15, "Hungary")
# egor.tellAboutSelf()
egor.drinkAlcohol()

    
    