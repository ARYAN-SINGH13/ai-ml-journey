# Day 1 - Python Basics Practice
# Author: Aryan Singh
# Topic: Variables, Input/Output, Conditions

print("AI/ML Journey - Day 1")

# Variables
name = "Aryan Singh"
age = 18
goal = "Become an AI/ML Engineer"

print("Name:", name)
print("Age:", age)
print("Goal:", goal)

# Taking user input
user_name = input("Enter your name: ")
print("Welcome", user_name)

# Simple condition
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")

print("Day 1 practice completed.")
