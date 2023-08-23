#!/usr/bin/env python3

# Created By: Jake@Linux
# Created On: Fri 11 Aug 2023 08:59:50 AM CDT
# Project: display only even numbers in given range

num1 = int(input("select first number: "))
num2 = int(input("select second number: "))

value = range(num1, num2)
num = 0
for i in value:
    if i % 2 == 0:
        print(i)
        num += 1
print(num, "numbers")
