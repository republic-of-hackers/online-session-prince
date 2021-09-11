'''
    A book publisher conducted a survey and found that 70% of the teenagers love to read fiction novels. The
    population of the area that the publisher can cover is 500000, out of which 40% are teenagers. The
    publisher earns a profit of Rs10 on the sale of each copy of a fiction novel. Write Python script to find
    maximum profit that the publisher can earn by selling copies of one fiction novel to teenagers.

    total population - 500000
    teenagers population -  200000 ( 40 % of total population)
    teenagers like to read fiction novel - 140000 ( 70 % of teenager population)
    profit on 1 copy sale - Rs10
    max profit of saling single fiction novel - 140000 * 10 = 1400000
'''
# Procedures
# 1) analyse input in program.
# 2) analyse output in program.
# 3) analyse logic in program.

# analyse input -> total_population - 5 lakh, profit_rate 
# analyse output -> max_profit
# analyse logic -> 
# analyse calcution -> teenager_population, teenager_likes_fiction, max_profit

# double analyse on logic
'''
    total population - 500000
    teenagers population -  200000 ( 40 % of total population)
    teenagers like to read fiction novel - 140000 ( 70 % of teenager population)
    profit on 1 copy sale - Rs10
    max profit of saling single fiction novel - 140000 * 10 = 1400000
'''

# Program

# Input
total_population = 500000
profit_rate = 10

# Calculation
teenager_population = total_population*.4
teenager_likes_fiction = teenager_population*.7

# Logic
max_profit = teenager_likes_fiction * profit_rate

# Ouput
print("In total population of", total_population, "having total teenager population as", teenager_population, "in which teenagers like fiction novel are", teenager_likes_fiction, "can product maximum profit of", max_profit, "Rupees. At a rate of", profit_rate, "Rs. per sale.")



