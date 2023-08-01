#Q.11) Write a program to replace comma-seprated words with
# hypens and print hypen-seprated words in asending order

str="G,Z,J,E,C,U,I,K"
str1=str.split(",")
str1.sort()
print(str1)

str2 = "_".join(str1)

print(str2)