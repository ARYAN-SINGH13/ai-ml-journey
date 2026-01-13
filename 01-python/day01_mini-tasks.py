# Day 1 - Mini Tasks Practice
# Author: Aryan Singh
# Topics: Input, Conditions, Basic Logic

print("AI/ML Journey - Day 1 Mini Tasks\n")

# ---------------------------
# 1. Age Eligibility Checker
# ---------------------------
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ---------------------------
# 2. Positive, Negative or Zero
# ---------------------------
num = int(input("\nEnter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# ---------------------------
# 3. Largest of Two Numbers
# ---------------------------
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

# ---------------------------
# 4. Pass or Fail System
# ---------------------------
marks = int(input("\nEnter your marks: "))

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

# ---------------------------
# 5. Even or Odd Checker
# ---------------------------
number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ---------------------------
# 6. Mini Calculator
# ---------------------------
print("\n--- Simple Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation")

print("\nDay 1 mini tasks completed successfully.")
