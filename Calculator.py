"""This is a program that acts as a calculator. It will be able 
to take complex numbers and do calculations on them.
"""
import math

#Step 1: Take an input from the user and save them to a variable.
input_str = input("What do you want calculated? (i.e. 20 - 3): ")
parts = input_str.split()
number1 = parts[0]
operator = parts [1]
number2 = parts[2]

#Step 3: Based on the selection, create a decision flow tree
if parts[1] == '+':
    value = number1 + number2
elif parts[1] == '-':
    value = number1 - number2
elif parts[1] == '*':
    value = number1 * number2
elif parts[1] == '/':
    value = number1 / number2

print(f"The result equals: {value}") 


#Step 4: Create the return value

#Step 5: Print the value
