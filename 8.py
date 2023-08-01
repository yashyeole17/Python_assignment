# Q8 Write Python Code to Determine Whether the Given String Is a Palindrome or Not Using Slicing
def is_palindrome(string):

    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True

#user-define
str=input("Enter string to check palindrome or not: ")
print(is_palindrome(str))

#pre-define
#print(is_palindrome("racecar"))  # True
#print(is_palindrome("hello"))    # False
#print(is_palindrome("12321"))    # True

