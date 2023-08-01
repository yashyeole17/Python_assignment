#Q5 Write Python Program to print n prime numbers.

no=int(input("Enter no to check prime or not: "))
for i in range(2,no):
    if no%i==0:
        print("No is not prime")
        break
else:
    print("No is prime")
