'''
For Loop

syntax - how to write it

keyword - for, in
function - range
identifier - i or any other

example:

for i in range(10):
    -- statments --

'''
# Table of 19
# for i in range(1, 11):
#     print("19 X", i , "=", 19*i)

# for i in range(1, 101, 2):
#     print(i, ",", end='')

'''
While Loop

syntax

while condition:
    -- statements --
'''
# i = 1
# while i <= 10:
#     print("19 X", i , "=", 19*i)
#     i = i + 1

'''
break & continue
'''
i = 1
while i < 100:
    print(i)
    i = i + 1
    if i > 28:
        break
print("end of loop")

i = 0
while i < 100:
    i = i + 1
    if i < 20:    
        continue
    print(i)
    # st1
    # st2