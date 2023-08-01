#Q7 Write a Program to Find the Sum of All Odd and Even
#Numbers up to a Number Specified by the User. Using functions

def add1(no):
    total_even=0
    for i in range(1,no+1):
        if i % 2 == 0:
            total_even+=i
    return total_even


def add2(no):
    total_odd=0
    for i in range(1,no+1):
        if i % 2 == 1:
            total_odd+=i
    return total_odd

no=int(input("enter no: "))
total_even=add1(no)
total_odd=add2(no)

print("",total_even)
print("",total_odd)



