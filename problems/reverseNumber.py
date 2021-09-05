# Write a Python Program to Reverse a Given Number
# 123 -> 321 

# Procedures
# 1) analyse input in program.
# 2) analyse output in program.
# 3) analyse logic in program.

# analyse input - Number (n)
# analyse output - Reverse Number (rn)
# analyse logic - Convert the number places from source to destination

# double analyse on logic
# 123 -> _
# 12 -> 300
# 1 -> 320
# _ -> 321

# Program
n = int(input("Enter a number: "))
rn = 0

# # Iteration 1
# reminder = n % 10 # 3
# qoutaint = n // 10 # 12

# rn = rn*10 + reminder # 3
# n = qoutaint # 12

# # Iteration 2
# reminder = n % 10 # 2
# qoutaint = n // 10 # 1

# rn = rn*10 + reminder # 32
# n = qoutaint # 1

# # Iteration 3
# reminder = n % 10 # 1
# qoutaint = n // 10 # 0

# rn = rn*10 + reminder # 321
# n = qoutaint # 0

# LOOP
while n != 0:
    print("Iteration")
    reminder = n % 10
    rn = rn*10 + reminder
    n = n // 10

print(rn)



