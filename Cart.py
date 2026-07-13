class shoppingCart:
    def __init__(self,customerName):
        self.customerName=customerName
        self.cart=[]

    def addItem(self,item):
        self.cart.append(item)
        print(f"Items {item} added successfully")

    def removeItem(self,item):
       if item in self.cart:
           self.cart.remove(item)
       else:
           print("item not found")

    def showCart(self):
        for item in self.cart:
            print(f"show cart {item}")


customerName=input("enter your name")
shop=shoppingCart(customerName)
while True:
    print("1.Add cart")
    print("2.Remove cart")
    print("3.Show cart")
    option=input("select any option")
    if option=="1":
        item=input("enter item")
        shop.addItem(item)
    elif option==2:
        item = input("remove item")
        shop.removeItem(item)
    elif option=="3":
        shop.showCart()