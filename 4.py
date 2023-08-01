#Q4 Write a Program to Read marks from user and Find the percentage of marks of student

list1=[]
total=0
number=int(input("Enter no. of subjects for you want to calculate percentage: "))
for i in range(number):
    marks=float(input("Enter marks for subject: "))
    list1.append(marks)
for i in list1:
    total+=i
percentage=(total/(number*100)*100)
print("Total: ",total)
print("Percentage: ",percentage,"%")
