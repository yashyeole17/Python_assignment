#21 triangle

for i in range(1,6):
    j=5-i
    while j>0:
        print(" ", end=" ")
        j-=1
    k=1
    while k<=i:
        print(" * ",end=" ")
        k+=1
    print()
