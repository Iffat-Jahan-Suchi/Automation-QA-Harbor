class sellerInfo:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def commission(self):
        ab=self.salary*15//100
        final=self.salary+ab
        print(f"After 15% commission fixed salary is {final}")
name=input("Enter your name ")
salary=float(input("Enter salary"))
seller=sellerInfo(name,salary)
seller.commission()