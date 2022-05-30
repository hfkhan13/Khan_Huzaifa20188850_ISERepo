from productioncode import *

# Module 1 Category 1a)
print("Testing Category 1a) Converting string to upper case:\n")
print("Test Data Input: Khan")
print("Output: " + convert_to_upper("Khan"))  
print("\n")

# Test category 1a
print("Testing Category 1a) Converting string to lower case:\n")
print("Test Data Input: Huzaifa Faisal Khan")
print("Output: " + convert_to_lower("Huzaifa Faisal Khan")) 
print("\n")

# Module 2 Category 1b)
print("Testing Category 1b) Checking if string contains a numeric value:\n")
print("Test Data Input: I am 20 years old")
print("Output: ", end="")
contains_numeric("I am 20 years old")
print("\n")

#Test Category 1b
print("Testing Category 1b) Checking if string contains a numeric value:\n")
print("Test Data Input: Pirates of the Caribbean")
print("Output: ", end="")
contains_numeric("Pirates of the Caribbean")
print("\n")

# Module 3 Category 1c)
print("Testing Category 1c) Checking if string is a valid number:\n")
print("Test Data Input: 2p67hello")
print("Output: ", end="")
valid_number_checker("2p67hello")
print("\n")

# Test Category 1c
print("Testing Category 1c) Checking if string is a valid number:\n")
print("Test Data Input: 8850")
print("Output: ", end="")
valid_number_checker("8850") 
print("\n")

# Module 4 Category 1d)
print("Testing Category 1d) Removing numeric values from string and converting it to upper case")
print("Test Data Input: I am 20 twenty years old")
print("Output: " + remove_number_upper("I am 20 twenty years old"))
print("\n")

# Test Category 1d
print("Testing Category 1d) Removing numeric values from string and converting it to upper case")
print("Output: " + remove_number_lower("I am 20 twenty years old"))
print("\n")


print("60 hours is " + str(hours_to_minutes(60)) + " minutes")#  test category 2 c)

print("60 minutes is " + str(minutes_to_hours(60)) + " hours")#  test category 2 c)


print("60 minutes is " + str(minutes_to_seconds(60)) + " seconds")#  test category 2 c)


print("60 seconds is " + str(seconds_to_minutes(60)) + " minutes")#  test category 2 c)
