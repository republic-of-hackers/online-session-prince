# Write Python script to input two numbers from the user and store these values in two different
# variables. Then interchange (swap) the values of these two variables using a third variable.
var1 = int( input("Enter var1 = "))
var2 = int( input("Enter var2 = "))

print("var1=", var1)
print("var2=", var2)

print("EXCHANGING VARIABLES...")

# var3-> 5 and var1-> 5
var3 = var1

# var1->2 and var2-> 2
var1 = var2

# var2->5 and var3-> 5
var2 = var3

print("var1=", var1)
print("var2=", var2)