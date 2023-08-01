# Q1.1 Write a program to read number from user and check its even or odd
num1=int(input("Enter no to check even or odd: "))
if num1 % 2 ==0:
    print(f"{num1} is even")
elif num1 % 2 != 0:
    print(f"{num1} is odd")
