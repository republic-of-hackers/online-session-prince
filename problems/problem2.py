'''
    A student has to travel a distance of 450 km by car at a certain average speed . write python program to
    find the total time taken to cover the distance.
    Formula:
    Time= Total Distance/Average speed

'''

# Procedures
# 1) analyse input in program.
# 2) analyse output in program.
# 3) analyse logic in program.

# analyse input -> distance - 450 km, avg speed
# analyse output -> time
# analyse logic -> calculate time

# double analyse on logic
# Time = Total Distance / Average speed

# Program

# Input
distance = 450
speed = float(input("Enter average speed (km/h): "))

# Logic
time = distance / speed

# output
print("Time taken to cover a distance", distance, "km with average speed", speed, "km/h is", time, "hrs.")
