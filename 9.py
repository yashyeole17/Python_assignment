# Q9 Program to Print the Characters Which Are Common in Two Strings
str1=input("Enter 1 string: ")
str2=input("Enter 2 string: ")
count=0
for i in str1:
    for j in str2:
        if i==j:
            print(i)
            count+=1
            break
print("Common characters: ",count)