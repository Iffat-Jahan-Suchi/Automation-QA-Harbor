# Build a program to determine if a year is a leap year

try:
    year = int(input("Enter year "))

    if year % 400 == 0:
        print("leap year")
    elif year % 100 == 0:
        print("not leap year")
    elif year % 4 == 0:
        print("leap year")
    else:
        print("not leap year")
except ValueError:
    print("year should be an integer number")
