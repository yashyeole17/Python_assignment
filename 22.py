#Q.22) Write a python program that accepts a sentence as input and
# removes all duplicate words . Print the sorted order using function

def duplicates(s):
  words=s.split()
  unique_words=list(set(words))
  sorted_words=sorted(unique_words)
  return " ".join(sorted_words)

sent = input("Enter a sentence: ")
s=sent.lower()
d1=duplicates(s)
print(d1)