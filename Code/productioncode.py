'''

METHOD: convert_to_upper and convert_to_lower
IMPORT: a string parsed into the module
EXPORT: a string that has been converted into all upper cases and into all lower cases
ASSERTION: converts a string to one that has been converted into all upper case letters and lower cases

'''

def convert_to_upper(string):
    string = string.upper()
    return string

print(convert_to_upper("i am huzaifa"))  #test category 1a

def convert_to_lower(string):
    string = string.lower()
    return string

print(convert_to_lower("I Am Huzaifa"))  #test category 1a

'''

METHOD: contains_numeric
IMPORT: a string parsed into the module
EXPORT: a string that checks whether it contains a numeric or not
ASSERTION: converts a string to indicate whether there are numeric values or not

'''

def contains_numeric(string):
    number_in_string = False
    for letter in string:
        if letter.isdigit() == True:
            number_in_string = True
    if number_in_string == True:
        print("There are numeric values in this string")
    else:
        print("There are no numeric values in this string")
    
contains_numeric("I am 20 years old") #test category 1b
contains_numeric("I am twenty years old") #test category 1b

'''

METHOD: valid_number_checker
IMPORT: a string parsed into the module
EXPORT: a string that checks whether it contains a valid number or an invalid number
ASSERTION: converts a string to indicate whether there is a valid number in it or an invalid number

'''

def valid_number_checker(string):
    if string.isnumeric():
        print("This is a valid number")
    else:
        print("This is not a valid number")
        
valid_number_checker("2p67hello")#  test category 1 c)
valid_number_checker("2670") #  test category 1 c)

'''

METHOD: remove_number_upper and remove_number_lower
IMPORT: a string parsed into the module
EXPORT: a string that removes a number and has been converted into all upper cases and lower cases
ASSERTION: converts a string to one that has been converted into all upper case letters and lower cases with no numbers

'''
def remove_number_upper(string):
    string = ''.join([i for i in string if not i.isdigit()])
    return string.upper()

def remove_number_lower(string):
    string = ''.join([i for i in string if not i.isdigit()])
    return string.lower()

print(remove_number_upper("I am a 20 twenty years old"))#  test category 1 d)


print(remove_number_lower("I am a 20 twenty year old"))#  test category 1 d)

'''

METHOD A: hours_to_minutes and minutes_to_hours
METHOD B: minutes_to_seconds and seconds_to_minutes
IMPORT: a string parsed into the module
EXPORT A: a string that has been converted from hours to minutes and minutes to hours
EXPORT B:  a string that has been converted from minutes to seconds and seconds to minutes
ASSERTION: converts a string to one that has been converted from hours to minutes and vice versa, and minutes to seconds and vice versa

'''
def hours_to_minutes(hours):
    minutes = hours*60
    return minutes
print("60 hours is " + str(hours_to_minutes(60)) + " minutes")#  test category 2 c)

def minutes_to_hours(minutes):
    hours = minutes/60
    return hours
print("60 minutes is " + str(minutes_to_hours(60)) + " hours")#  test category 2 c)

def minutes_to_seconds(minutes):
    seconds = minutes*60
    return seconds
print("60 minutes is " + str(minutes_to_seconds(60)) + " seconds")#  test category 2 c)

def seconds_to_minutes(seconds):
    minutes= seconds/60
    return minutes
print("60 seconds is " + str(seconds_to_minutes(60)) + " minutes")#  test category 2 c)
