class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_salary(self):
        print(f"Current Salary is {self.salary}")

    def increase_salary(self,amount):
       amount=self.salary+amount
       print(f"in is {amount}")

em=employee("lll",5400)
em.display_salary()
em.increase_salary(500)