#Q10     Python Program to Count the Total Number of Vowels, Consonants and Blanks in a String

vovels,blanks,consonants=0,0,0
str=input("Enter the string: ")
for char in str:
    if char =='a' or char =='e' or char =='o' or char =='i' or char =='u': 
        vovels+=1
        
    elif char==" ":
        blanks+=1
        
    else:
        consonants+=1
        
print("No of VOVELS: ",vovels)
print("No of BLANKSPACE: ",blanks)
print("No of CONSONANTS: ",consonants)
