# Q16 Write a Python Program That Accepts a Sentence as Input and
# Removes All Duplicate Words. Print the Sorted Words



sent = input("Enter a sentence: ")

words = sent.split()
unique_words = list(set(words))
sorted_words = sorted(unique_words)
print(" ".join(sorted_words))