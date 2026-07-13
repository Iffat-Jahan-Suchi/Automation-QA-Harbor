from animal import Animal

class cat(Animal):
    def mew(self):
        print(f"{self.name} is sleeping")

name=input("enter animal name ")
newCat=cat(name)
newCat.eat()
newCat.mew()