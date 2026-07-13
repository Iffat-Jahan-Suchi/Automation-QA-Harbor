class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def booninfo(self):
        print(f"Book title is {self.title},Author name {self.author}"
              f"price is {self.price}")
    def discount(self,percentage):
        percentage=(self.price*percentage)//100
        afterDiscountAmount=self.price-percentage
        print(f"after percentage book amount {afterDiscountAmount}")
title=input("enter book title ")
author=input("enter book author ")
price=int(input("enter book price "))

book=book(title,author,price)
book.booninfo()
try:
    discount = input("Enter discount percentage: ")
    discount = discount.replace("%", "")
    selfPercentage = float(discount)

    book.discount(selfPercentage)

except ValueError:
    print("Please enter a valid percentage.")
