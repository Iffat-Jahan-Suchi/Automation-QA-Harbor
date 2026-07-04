# Write program to check if number is positive, negative, or zero;
# Handle invalid input for number input
try:
    number = int(input("enter your number "))
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is Negative")
    else:
        print("Number is 0")
except ValueError:
    print("Invalid input! Please enter a valid integer.")