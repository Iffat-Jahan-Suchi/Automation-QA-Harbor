from random import random

a=float(input("Enter first number "))
b=float(input("Enter Second number "))
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
res=sum(a,b)
res1=sum(a,b)
res2=mul(a,b)
res3=div(a,b)
print(f"sum is {res}")
print(f"sub is {res1}")
print(f"mul is {res2}")
print(f"div is {res3}")



# #Write function to calculate square of a number;

a=int(input("Enter your number "))
def square(a):
    return a*a
print(square(a))

#Create dice-rolling simulator with random module;
dice = int(random() * 6) +1
print("dice-rolling:", dice)

#palindrome
num = 0
temp = 0
r = 0
sum = 0
num = int(input("Enter any number: "))
temp = num
while temp!=0:
    r=temp%10
    sum=sum*10+r
    temp= temp//10
if num==sum:
    print("Palindrome number")
else:
    print("Not a palindrome")

#Build a number-guessing game using functions and random module
try:
    def userInput():
        guess = int(input("Enter any number from 1 to 6: "))
        return guess
    guess = userInput()
    actualNumber = int(random() * 6) + 1
    if guess <= 0 or guess > 6:
        print("Please enter a number between 1 and 6.")
    elif guess == actualNumber:
        print("won")
    else:
        print(f"failed!number was {actualNumber}")
except ValueError:
        print("Please enter a valid number.")

#password
special = "!@#$%^&*"
password = input("Enter password: ")
found = False
for i in password:
    if i in special:
        found = True
        break
if len(password) != 8:
    print("Password must be exactly 8 characters.")
elif found:
    print("Login...")
else:
    print("Password must contain at least one special character.")


