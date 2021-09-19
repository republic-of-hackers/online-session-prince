'''
    Write a program that input three numbers and calculates two sums as per this
        a. As the sum of all input numbers
        b. As the sum of non-duplicate numbers; if there are duplicate numbers in the input, ignore
            them.
'''

#Program

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

# Part a
s = a + b + c
print("Sum of all input numbers", s)

# Part b
'''
    a = b = c -> print(a)
    a = b and b != c | b distinct -> print(b+c) or print(a+c)
    a = c and c != b | c distinct -> print(c+b) or print(a+b)
    b = c and a != b | a distinct -> print(a+b) or print(a+c)
'''
if a == b:
    if b != c:
        print(b+c)
    else:
        print(a)
else:
    if b == c:
        print(a+b)
    else:
        print(a+b+c)
