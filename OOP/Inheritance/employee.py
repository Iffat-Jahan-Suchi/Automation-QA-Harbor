class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_salary(self):
        print(f"Name is {self.name},Salary is {self.salary}")
class Manager(Employee):
    def __init(self,department):
        # super().__init__(name, salary)
        self.department = department
    def showManager(self):
        super().show_salary()
        print(f"Department is {self.department}")


name=input("enter your name")
salary=float(input("enter your salary"))
department=input("Enter your department")

manager=Manager(name,salary)
manager.show_salary()
manager.showManager()
