# **ISAD1000 Assignment**
# Huzaifa Khan 20188850
# CURTIN UNIVERSITY SEMESTER ONE 2022
# PRACTICAL CLASS: WEDNESDAY 10-12; 314.218

## **Introduction**
The purpose of this report is to display and convey certain software engineering techniques and use these techniques to describe and implement code correctly. The code that will be used for this software program is Python. document gives a thorough explanation and description on how software engineering techniques were implemented. Each technique influences the other, and various testing techniques were also used to refine and correct the code. The skills that will be shown are as follows: converting a string into upper or lower case (category 1a), identifying whether numeric values are in a given string (category 1b), identify whether a given string is a valid number or not (category 1c), remove any numeric values in a given string and then convert the string to upper case or lower case (category 1d) and converting a number which represents a time given in hours to minutes and vice versa and time given in minutes to seconds and vice versa (category 2c). This document provides a description of the modules created, and touches on the modularity aspects that were applied in the code, as well as two types of testing techniques that were used (black box and white box testing) to implement the test code. Ethics and Professionalism is another key area that this report discusses and describes using the code designed in the report in a large-scale scenario, and what the lack of ethics and professionalism could lead to. 

## **Module Descriptions**
In this description, sub-parts of the program will be described, and it will convey how the modules will successfully do the job that the scenario requires. However, they will all be under one main program, which will be called productioncode.py. In this umbrella program, the modules that will be described are sub-parts of the program, that are all doing similar tasks and using similar functions and techniques to complete those tasks correctly.

## *Module 1:(Category 1a)*
### Name: Upper and Lowercase Module
### Method A: convert_to_upper
### Method B: convery_to_lower
### Input: A string is parsed into the module.
### Output A: A string that has been converted into all upper-case letters.
### Output B: A string that has been converted into all lower-case letters.
### Assertion A: Converts a string to one that has been converted into all upper-case letters.
### Assertion B: Converts a string to one that has been converted into all lower-case letters.

## *Module 2:(Category 1b)*
### Name: Numeric Value Module
### Method: contains_numeric
### Input: A string is parsed into the module.
### Output: A string that checks whether it contains a numeric value or not.
### Assertion A: Converts a string to indicate that there are numeric values present.
### Assertion B: Converts a string to indicate that there are no numeric values present.

## *Module 3:(Category 1c)*
### Name: Valid Number Module
### Method: valid_number_checker
### Input: A string is parsed into the module.
### Output: A string that checks whether it contains a valid number or not.
### Assertion A: Converts string to indicate a valid number.
### Assertion B: Converts string to indicated invalid number.

## *Module 4:(Category 1d)*
### Name: Numeric Upper and Lower Module
### Method A: remove_number_upper
### Method B: remove_number_lower
### Input: A string is parsed into a module.
### Output A: A string that removes a number and has been converted into all upper-case letters.
### Output B: A string that removes a number and has been converted into all lower-case letters.
### Assertion A: Converts a string to one that been converted into all upper-case letters with no numbers.
### Assertion B: Converts a string to one that been converted into all lower-case letters with no numbers.



## *Module 5:(Category 2c)*
Converting a number which represents a time given in hours to minutes and vice versa, and time given in minutes to seconds and vice versa.

### Name: Time changing module
### Method A: hours_to_minutes and minutes_to_hours
### Method B: minutes_to_seconds and seconds_to_minutes
### Import: A string is parsed into the module
### Output A: A string that has been converted from hours to minutes and minutes to hours.
### Output B: A string that has been converted from minutes to seconds and seconds to minutes.
### Assertion A: Converts a string to one that has been converted from hours to minutes and vice versa
### Assertion B: Converts a string to one that has been converted from minutes to seconds and vice versa.

## **Modularity**
Using the above module descriptions of the modules that have been designed, a program was created using the coding language Python so that each module is performing its task correctly without any errors.

### Description on how to run code with correct commands: 
The code that was implemented based off the module descriptions used the coding language python. For each module, the descriptions on how to run the code is given below.

## **Module 1:**
The first line of the code “def convert_to_upper(string)” is used to define the string that is going to be used in the module. It defines what the method will be in the module, which to “convert_to_upper” and defines that for the string. The second line of the code allows the module to convert the string into all upper-case letters, by the function “upper()”, which is part of the intended task of the module. “The return string function” then parses the string through the module. After that, the print() function is used to convey that the task intended has been correctly implemented without any errors when the code is run, and the sentence in the string “i am huzaifa” returns as “I AM HUZAIFA” when the code is run. To convert a string to all lower-case letters, the exact same thing is implemented, however the method is changed from “convert_to_upper” to “convert_to_lower”, and the function “lower()” is used and parsed through the string. 

## **Module 2:**
In the first line of the code (screenshot of the code is shown below), the string is defined as “def contains_numeric(string)”. The “number_in_string” function allows the string to convey that if it does not contain a numeric number, then it will be “false”. To find whether there are numeric values in the string, we use the isdigit() method. This method returns a true value if there are valid numeric values in the string and returns false if there are no numeric values. Numeric values in this case refer to number only. For example, 20 would be considered a numeric value in the string, however twenty would not. The == signs compare the two sentences that will be checked for numeric values and compares them to see if they give the same value. The “if” indicates whether the expression is true or false; in this case whether there are numeric values or not. If there are numeric values in the string, the print() functions allow for this to be shown and prints “There are numeric values in the string”. If there aren’t any numeric values, the else function is utilised to figure out what to do when the condition is not met; in this case “there are no numeric values” is printed. The last two lines of the module uses the contains_numeric to  check whether there are, or there are no numeric values in the given sentence


## **Module 3:**
The function “def valid_number_checker(string)” is used to define what the function is, and the method “valid_number_checker” is parsed through the string. In the second line of the code, isnumeric() is used to identify whether there is a valid numeric value in the given string, and an if statement is used to evaluate whether it is true or false. If there is a valid number, then the print function is used to print “This is a valid number”, otherwise if the criteria is not met, “This is not a valid number” is printed when the code is run. The last two lines of the code use the method “valid_number_checker” to check whether the given “numbers” are valid numbers or not; this is indicated when the code is run. The code is shown below.

## **Module 4:**
The first line of the module defines what method the module will be using and passing the string through the module; in this instance, the method “remove_number_upper” is used, which basically removes any numbers from the string and makes all the letters upper case. The second line of the code removes a character (in this case it removes all numeric values) and then joins the remaining string to make one string. This is then returned as one string with all upper-case letters using the upper() function. The second part of the code does the exact same thing as the first, however it turns the string into all lower-case letters with no numbers. This is then printed for both upper and lower in the last two lines of the code. Numeric values in this module are numeric digits only and do not apply to number that are written, such as “twenty”.

## **Module 5:**
This code offers a lot of reusable code, with only minor differences with each line of code. For the first part, the string is defined, and a simple calculation is written to convert hours to minutes. The return function is used to return hours that have been converted and the print function is used to indicated that there are “ 60 hours in 3600 minutes” when the code is run. The same method is applied when converting minutes to hours, however besides multiplying by 60, we divide by 60 and the print function is used to indicate the given result when the code is run. The same exact functions are used to convert minutes to seconds and vice versa in the second part of the code. A screenshot of module 5 is shown below for a better understanding on how the code is illustrated.

### *Discussion on different modularity concepts applied in code:* 
### While creating the program and writing the code, many modularity techniques were used to improve and make the code more efficient and to the standard of software engineering principles. A divide and conquer approach were used for all the modules. As illustrated in the code, the program runs all at once, however different parts of the code do different tasks; each sub-part of the program performs its own well-defined task. This is clearly shown through using labels above each module, as well as spacing each module out and diving problems into smaller ones and tackling them from the ground up. Every module in the code applies this strategy which made writing the code much easier and allowed for the task of each module to be carried out without many problems. Coupling is a technique that is prevalent in coding. We can see that each module performs its task on its own and is not dependant and reliant on any other module. The content of each module is vaguely connected to each other, for instance similar lines of code might have been used to perform different tasks. However, the internal workings of each module are not shown to another module, and they do not have a significant effect on each other. The code is simple and does not dive into the complexity of python. This shows that there are not that many global variables present, as the use of global variables increase the complexity of the code. This is also shown as in almost every module, return values and parameters are used to import and export information, such as the lines of code shown below.

### As shown above, the use of parameters and a return value removes the possibility of having global values. The modules are all very cohesive, as they all perform their specific task precisely and efficiently. As stated above, low/loose coupling is present in the program, which goes hand in hand with high cohesion. Each task is separated into its separate modules that are labelled and illustrated, so that code does not get mixed up and the task of each module is clearly illustrated as well; this indicates high cohesion. The tasks of each module are related to each other in the sense that they all use the same sort of data, for instance they all parse a string through the module and use return values, parameters and if and else statements where applicable. Another technique used was the reuse of code throughout the program. This is different from redundancy and repetition, as even though the code is similar, it performs a different task and is needed for the requirement for each module to be met. An example of this is show below. 

### Yes, there is repetition and redundancy in the program, but any avoidable redundancy was avoided. These modularity concepts are applied throughout the program to make the code run smoothly and for the tasks of each module to be performed without any errors.

## **Review Checklist:**
1.	Has overlapping code been replaced/deleted to reduce repetition?
#### Yes, the code was written as such that modules are not using the exact same code each time; however, some do have similar lines of code performing different tasks

2.	Has code been re-used to perform tasks for different modules?
#### Yes, there is not an extreme amount of repetition in the code, and the code that has been repeated has been reused for similar but not the same tasks.

3.	Are all modules split-up into their respective well-defined tasks?
#### Yes, each module is split up and above each module is a brief explanation as to what the intended task of the module is

4.	Are all modules performing one well-defined task effectively?
#### Yes, each module performs its task without any problems.

5.	Are methods/functions using parameters?
#### Yes

6.	Are methods/functions using return values?
#### Yes

7.	Is each string returned in every module?
#### Yes

8.	At the end of each module, is the string “printed” to indicate that the required task of the module has been implemented when the code is run?
#### Yes, using the print() function

9.	Is each string defined at the start of each module?
#### Yes, using the “def()” function.
10.	Is each string parsed through their respective module?
#### Yes

As shown in the checklist above, from the questions that have been derived, there was no refactoring needed to be done, and any issues that came up are shown and logged in the gitlog and version control. The code has been kept simple and concise to avoid any major issues from occurring, and hence no issues arose, and refactoring was not needed for this program.

## **Black-box Test Cases:**
### **Module 1:**
| Category                    |  Test Data             |  Expected Result
| :---                        |    :----:              |              ---:
| String is a valid string    | "Khan"                 |  KHAN
| String is an invalid string | "Huzaifa Faisal Khan"  |  huzaifa faisal khan

### **Module 2:**
| Category                         |  Test Data             |  Expected Result
| :---                             |    :----:              |              ---:
| String contains a numeric value  | “I am 20 years old”    |  There are numeric values in this string
| String contains no numeric value | "Pirates of Caribbean" |  There are no. numeric values in this string

### **Module 3:**
| Category                    |  Test Data             |  Expected Result
| :---                        |    :----:              |              ---:
| String is an invalid number | “2p67hello”            |  This is not a valid number
| String is a valid number    | “8850”                 |  This is a valid number

### **Module 4:**
| Category                                               |  Test Data                  |  Expected Result
| :---                                                   |    :----:                   |              ---:
| String is a valid string and contains a numeric value  | “I am 20 twenty years old”  |  I AM TWENTY YEARS OLD
| String is a valid string and contains a numeric value  | “I am 20 twenty years old”  |  i am twenty years old


### **Module 5:**
| Category                           |  Test Data             |  Expected Result
| :---                               |    :----:              |              ---:
| String converts hours to minutes   |    “hours*60”          |  60 hours is 3600 minutes            
| String converts minutes to hours   |    “minutes/60”        |  60 minutes is 1 hour
| String converts minutes to seconds |    “minutes*60”        |  60 minutes is 3600 seconds
| String converts seconds to minutes |    “seconds/60”        |  60 seconds is 1 minute