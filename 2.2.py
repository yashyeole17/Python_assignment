#Q2.2 Write Python Program to Find the Sum of Digits in a Number

num1=int(input("Enter no to add digits ( number> 0): "))
sum = 0
while num1>0:
    digits= num1%10
    sum += digits
    num1//=10
print("Sum of ditits if given number: ",sum)