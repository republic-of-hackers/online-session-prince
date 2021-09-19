'''
    Write a program to find the age group for given age by a user.

    Range           Age Group
    0-3(incl)       Infant Group
    3-18(incl)      Teenage Group
    18-40(incl)     Adult Group
    40+             Old Group
'''

age = int(input("Enter your age: "))

if age >= 0 and age <= 3:
    print("Infant Group")
elif age > 3 and age <= 18:
    print("Teenage Group")
elif age > 18 and age <=40:
    print("Adult Group")
else:
    print("Old Group")