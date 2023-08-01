#Q6  Write a Program to Display the Fibonacci Sequences up to
# nth TermWhere n is Provided by the User
nth=int(input("Enter no of term to print: "))
a,b=0,1
if nth==a:
    print(a)
else:   
    for i in range(0,nth):
        print(a)
        a,b=b,a+b
