'''
    Mahmood has taken some loan from Ashraf at a certain rate of simple interest. After 6 years
    Mahmood wants to repay the loan in full and final including interest. Write Python code to calculate
    and display the interest and total amount to be paid by Mahmood to settle the account.
'''

# Procedures
# 1) analyse input in program.
# 2) analyse output in program.
# 3) analyse logic in program.

# analyse input - time - 6 yrs, Rate - ? , Principal - ?
# analyse output - interest, total amount
# analyse logic - to calculate interest and total amount

# double analyse on logic
# interest - simple interest & compound interest
# Simple Interest 
# Formula - Simple Interest = (Principal * Rate * Time) / 100
# Total Amount = Principal + Simple Interest

# Program

# Input Coding
time = 6
rate = float(input("Enter rate: "))
principal = float(input("Enter principal: "))

# Logic Coding
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

# Output Coding
print("Interest:", simple_interest)
print("Total Amount:", total_amount)