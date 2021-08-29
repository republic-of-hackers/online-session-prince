# Python Program to Read a Number n and Compute n + nn + nnn
# n = 10
n = int( input("Enter a number n: ") )

# temp = "10"
temp = str(n)

# t1 = "10" + "10" = "1010"
t1 = temp + temp

# t2 = "101010"
t2= temp + temp + temp

# comp = 10 + 1010 + 101010 = 102030
comp = n + int(t1) + int(t2)

print("The value is:",comp)

# Concatination
# "prince" + "sharma" = "princesharma"