#!/usr/bin/env python
# variables.py
# String
name = 'Aishwarya Deengar'

# Integer
age = 23

# List of strings
names = ["ABCD", "EFGH", "IJKL"]

# List of numbers
numbers = [15.5, 25.6, 50, 500]

# Dictionary of names and ages
ages = {'ABCD': 23, 'EFGH': 63, 'IJKL': 28}

# Print the values of the variables
print(name)
print(age)
print(names)
print(numbers)
print(ages)

# Find out what type Python assigned to the variables
print(type(name))
print(type(age))
print(type(names))
print(type(numbers))
print(type(ages))

# Iterate over names in a for loop
for name in names:
    print(name)
    print(type(name))
