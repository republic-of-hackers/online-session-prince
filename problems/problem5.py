'''
    Write a program to find the largest of 3 numbers. Number should be taken from user.
'''

# Procedures
# 1) analyse input in program.
# 2) analyse output in program.
# 3) analyse logic in program.

# analyse input -> 3 - numbers
# analyse output -> largest number
# analyse logic -> largest of 3 number

# double analyse on logic
'''
    a, b, c - 3 numbers
    a > b and a > c => a is largest
    b > a and b > c => b is largest
    c > a and c > b => c is largest
'''

# Program

# input
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

# logic & output
if a > b:
    if a > c:
        print("Largest number", a)
    else:
        print("Largest number", c)
else:
    if b > c:
        print("Largest number", b)
    else:
        print("Largest number", c)