class mobile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.battery=100

    def call(self):
        if self.battery>=10:
            self.battery=self.battery-10
            print("Calling....")
            print(f"Phone battery is {self.battery}%")
    def info(self):
        print(f"Brand name is {self.brand},model is {self.model},battery {self.battery}% ")
    def charge(self):
        self.battery=100
        print(f"Charge is {self.battery}%")
        print("100% charged")

brand=input("enter phone brand ")
model=input("enter model ")
myMobile=mobile(brand,model)
myMobile.info()

while True:
    print("\n1. call")
    print("2. Charge")
    print("3. Mobile info")
    print("4. Exit")

    option = input("input your option ")
    if option=="1":
        myMobile.call()
    elif option=="2":
        myMobile.charge()
    elif option=="3":
        myMobile.info()
    elif option=="4":
        print("Program End...")
        break
    else:
        print("Invalid option")

