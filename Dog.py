class dog:
    def __init__(self,age):
        self.age=age
    def bark(self):
        print(f"age is {self.age}")
    def birthday(self):
            self.age=self.age+1
            print(f"after birthday age  {self.age}")
for i in range (1,3):
    age = int(input("enter age "))
    dog = dog(age)
    dog.bark()
    dog.birthday()

