#Q.14) Write a python program to conduct a linear search for a given number
# in the list and report success or failure

list1 = [1,2,3,4,5,6,7,8,9,10]
n=int(input(" Enter a number "))

for i in range(len(list1)):
  if list1[i]==n:
    flag=1
    break
  else:
    flag=0

if flag==1:
  print("success")
else:
  print("failure")
