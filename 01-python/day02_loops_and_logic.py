# Day 2 - Loops and Logic Practice
# Author: Aryan Singh
# Topics: Loops, Conditions, Prime Numbers, Password System, Patterns

print("AI/ML Journey - Day 2\n")

# Day 2 - Loops and Logic Practice
# Author: Aryan Singh
# Topics: Loops, Conditions, Prime Numbers, Password System, Patterns

#A) Sum of numbers from 1 to n
n = int(input())

total = 0

for i in range(1,n+1):
    total += i
print(total)

#B) Count of even and odd numbers

#B)i)
lst = list(map(int,input().split()))

evn = 0
od = 0

for i in range(0,len(lst)):
    if lst[i] % 2 == 0 :
        evn += 1 
    else:
        od += 1
      
print(evn,od)

#B)ii)
lst = list(map(int,input().split()))

evn = sum(1 for x in lst if x %2 ==0)
od = sum(1 for x in lst if x%2 != 0)
print(evn,od)

# =====================================================
# Task 2 — Prime Numbers in Range
# Method A: Flag Method
# =====================================================

print("\nPrime numbers from 1 to 100 (Flag Method):")

start = 1
ends = 100

for num in range(start,ends +1):
    if num > 1:
        flag = 1 # assume number is prime

        for i in range(2,num):
            if num % i == 0 :
                flag = 0 # number is not prime
                break
        if flag == 1:
            print(num)

# =====================================================
# Task 2 — Method B: Optimized (sqrt method)
# =====================================================

print("Prime numbers in custom range (Optimized Method):")

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start,end + 1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)
          
print("\n")

# =====================================================
# Task 3 — Password Retry System
# =====================================================

print("Password Retry System")

correct_password = "python123"
attempts = 1

while attempts <= 3:
    user_input = input("Enter the password: ")

    if user_input == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password")
    
    attempts += 1

if attempts >=3:
    print("Account blocked")

# =====================================================
# Task 4 — Pattern Printing
# =====================================================

# Pattern A (Increasing stars)
print("\nPattern A:")

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


# Pattern B (Decreasing stars using while loop)
print("\nPattern B:")

n = int(input("Enter number of rows: "))

i = n
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i -= 1


print("\nDay 2 practice completed successfully.")
