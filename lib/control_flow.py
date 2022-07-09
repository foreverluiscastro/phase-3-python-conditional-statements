#!/usr/bin/env python3

import ipdb

def admin_login(username, password):
    # your code here
    pass
    if username == "admin" or username == "ADMIN":
        if password == "12345":
            return "Access granted"
        else:
            return "Access denied"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    # your code here
    pass
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    pass
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

fizzbuzz(4)

# def calculator(operation, num1, num2):
#     # your code here
#     pass
#     exceptions = ["+","-","*","/"]
#     if operation in exceptions:
#         ipdb.set_trace()

def calculator(operation, num1, num2):
#     # your code here
    pass
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

# calculator("+",1,1)
