#Create a program to greet user by name and calculate age based on birth year
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from playwright.sync_api import expect

# name=input("Enter your name ")
# birth_year=int(input("Enter your Birth year "))
# current_year = datetime.now().year
# age= current_year - birth_year
# print(f"Hello! {name},You are now {age} years old")


try:
    name = input("Enter your name ")
    if not name.isalpha():
        raise ValueError("Name must contain only letters.")
    birth_year = int(input("Enter your Birth year "))
    birth_month = int(input("Enter your Birth month "))
    birth_day = int(input("Enter your Birth day "))
    birth_date = date(birth_year, birth_month, birth_day)
    today = date.today()
    age = relativedelta(today, birth_date)
    print(f"Hello! {name},You age is {age.years} years,{age.months} months,{age.days}days")
except ValueError as e:
    print(f"Invalid input{e}")


