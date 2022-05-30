from productioncode import *

# Module 1 Category 1a)
print("Testing Category 1 a) Converting string to upper case:\n")
print("Test Data input: i am huzaifa")
print("Output: " + convert_to_upper("i am huzaifa"))  
print("\n")

# Test category 1a
print(convert_to_lower("I Am Huzaifa")) 

    
contains_numeric("I am 20 years old") #test category 1b
contains_numeric("I am twenty years old") #test category 1b

valid_number_checker("2p67hello")#  test category 1 c)
valid_number_checker("2670") #  test category 1 c)


print(remove_number_upper("I am 20 twenty years old"))#  test category 1 d)


print(remove_number_lower("I am 20 twenty years old"))#  test category 1 d)

print("60 hours is " + str(hours_to_minutes(60)) + " minutes")#  test category 2 c)

print("60 minutes is " + str(minutes_to_hours(60)) + " hours")#  test category 2 c)


print("60 minutes is " + str(minutes_to_seconds(60)) + " seconds")#  test category 2 c)


print("60 seconds is " + str(seconds_to_minutes(60)) + " minutes")#  test category 2 c)
