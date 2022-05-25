def convert_to_upper(string):
    string = string.upper()
    return string

print(convert_to_upper("i am huzaifa"))  #test category 1a

def convert_to_lower(string):
    string = string.lower()
    return string

print(convert_to_lower("I Am Huzaifa"))  #test category 1a

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