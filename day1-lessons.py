# The first program
print("Hello World!") # Basic print statement and printing a string
print(20) # Printing a number doesn't require qoutation


# Learning Variables
name = "Akshat Shaw" # Name variable containing String value
age = 20 # Age variable containing Int value
marks = 85.5 # Marks variable containing Float value


# Printing the variables
print(name)
print(age)
print(marks)


# Printing the types of the variables
print(type(name))
print(type(age))
print(type(marks))


'''
Types of Operators in python:
1. Arithmetic Operators: +, -, *, /, //, %, **      ||  Used to perform mathematical operations
2. Assignment Operators: =, +=, -=, *=, /=, //=, %=     ||  Used to assign values to variables
3. Comparison Operators: ==, !=, >, <, >=, <=       ||  Used to compare values between variables
4. Logical Operators: and, or, not      ||  Used to combine conditional statements
5. Identity Operators: is, is not     ||  Used to check if two variables are the same object
6. Membership Operators: in, not in   ||  Used to check if a value is present in a sequence
7. Bitwise Operators: &, |, ^, ~, <<, >>    ||  Used to perform bit-level operations
'''

'''
Operators Precedence in Python:
1. Parentheses: ()
2. Exponentiation: **
3. Unary plus and minus: +x, -x
4. Multiplication, Division, Floor Division, Modulus: *, /, //, %
5. Addition, Subtraction: +, -
6. Bitwise Shift Operators: <<, >>
7. Bitwise AND: &
8. Bitwise XOR: ^
9. Bitwise OR: |
10. Comparison Operators: ==, !=, <, >, <=, >=
11. Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=
12. Identity Operators: is, is not
13. Membership Operators: in, not in
'''


# Program to print the sum of two numbers
num1 = 5
num2 = 6
sum = num1 + num2 # Initializing a sum variable and assigning the sum of num1 and num2
print("The sum is " + str(sum))
print("The sum is " + str(num1 + num2)) # Alternative way to print the sum without using variable


# Expression execution
n, txt = 2, "Hello " # String and numeric values can operate together with * and + (Adding strings is called concatenation)
print(txt * n)
n1, n2 = 2, 2.5 # Arithmetic operations with integers and floats results in float
print(str(n1 + n2) + "  " + str(n1 * n2) + "  " + str(n1 / n2) + "  " + str(n1 - n2) + "  " + str(n1 % n2))
print(n1//n2) # Integer division, result is an integer but displays as float
''' Integer division is basically floor division from mathematics, it return the largest integer less than or equal to the reult.
For example 5//2 = 2.0. Even a number like 4.99 will be rounded down to 4.0 while being closest to 5'''

# Input function
name = input("Enter you name: ") # Input function is used to take input from the user
print("Hello " + name)
#** Input is always taken as string. So we use explicit type conversion to convert it to the datetype we want.
age = int(input("Enter your age: ")) # int() converts the input string to an integer type