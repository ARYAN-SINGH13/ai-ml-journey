# Day 1 - Python Basics Practice
# Author: Aryan Singh
# Topics: Variables, Data Types, Input/Output, Type Casting, Conditions

print("AI/ML Journey - Day 1\n")

# ---------------------------
# 1. Variables and Data Types
# ---------------------------

name = "Aryan Singh"          # string
age = 18                      # integer
height = 5.9                  # float
is_student = True             # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

print("\nData Types:")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# ---------------------------
# 2. User Input
# ---------------------------

user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))

print("Welcome", user_name)
print("Next year you will be", user_age + 1, "years old")

# ---------------------------
# 3. Simple Eligibility Check
# ---------------------------

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ---------------------------
# 4. Marks and Grade System
# ---------------------------

marks = int(input("\nEnter your marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Fail")

# ---------------------------
# 5. Even or Odd Check
# ---------------------------

num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# ---------------------------
# End
# ---------------------------

print("\nDay 1 practice completed successfully.")
