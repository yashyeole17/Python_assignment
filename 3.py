# Q3  Write a program to read percentage from user and print Grade
#percentage >=80 O
#percentage >=75 A+
#percentage >=70 A
#percentage >=65 B+
#percentage >=60 B
#percentage >=55 Pass

percent =int(input("Enter percentage:  "))
if percent>0 and percent<100:
    if percent >=80:
        print("Grade: O")
    elif percent >=75:
        print("Grade: A+")
    elif percent >=70:
        print("Grade: A")
    elif percent >=65:
        print("Grade: B+")
    elif percent >=60:
        print("Grade: B")
    elif percent >=55:
        print("PASS")
    else:
        print("FAIL")
        
    
