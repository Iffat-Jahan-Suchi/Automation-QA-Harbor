class employee:
    def __init__(self,name,salary,increment):
        self.name=name
        self.salary=salary
        self.increment=increment

    def displayInfo(self):
        print(f"NAme is {self.name},your salary {self.salary}")
    def updateSalary(self,increment):
        self.increment=self.salary+self.increment
        print(f"update salary {self.increment}")
name=input("enter your name ")
salary=int(input("enter your current salary "))
increment=int(input("enter increment amount "))

em=employee(name,salary,increment)
em.displayInfo()
em.updateSalary(increment)