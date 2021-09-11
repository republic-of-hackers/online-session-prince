# DataTypes in Python
'''
    Data + Type
    (the raw fact -> 123, "fdgfj", 3.45 etc) + (definition names -> Integer, String etc.)
'''
'''
    Numbers - Integer, Long, Float(Decimal), Complex Number
    String - eg: "name"
    List - ["prince", 17, 480.65]
    Tuple - ("Mon", "Tues", "Wed", "Thus", "Fri", "Sat", "Sun")
    *Dictionary (name->age) - {"prince": 17, "himanshu": "23"}
    Set (collection of unique entities is called Set.) - {1, 2, 3, 5, 6}
'''

# Numbers
# program 1 : Write a program to calculate the simple interest using P, R, T.
'''
    S.I = (P * R * T) / 100
'''
# P = 2000
# R = 8.5
# T = 1.5 # years

# SI = (P * R * T) / 100

# print(SI)

# String
# program 2: write a program to add word "AND" in between the first name and last name of the person.

# name = "Himanshu Sharma"

# # indicies
# ans = name[0:8] + " AND " + name[9:15]

# print(ans)

# List
# program 3: Write a program to store 1 record for class a students.
'''
    Student -
        name
        age
        class
        marks
        father name
        mother name
        resident
        city
        state
        country
        pincode
'''

# always start with 0
#record = ["prince", 17, "11th Class", 93.67, "sharma", "sharma", "Sec", "Faridabad", "HRY", "INDIA", 121001]
# indicies

# print("List:")
# record[0] = "Aku"
# record[1] = 9
# record[2] = "2nd Class"
# print(record)

# Property - Mutable (That can be changable.)

# Tuple

# always start with 0
# weekdays = ("Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat")

#indices
# print()
# print("Tuple:")
# print(weekdays)

# Property - Immutable (That can not be changable.)

# Set
# Declaration
# A = {1,2,3,5,5,7,8,9,0,0,5}
# print(A)

# Dictionary
# Declaration Key - Value
phone_book = {"Sharma": "0134567567", "Prince": "567889032", "aku": "74983478237"}

print(phone_book["Sharma"])
print(phone_book["Prince"])

# Exclusive
# default - DICT
t = {}

# constructor
B = set()
work_book = dict()
t_list = list()
tu_tuple = tuple()
