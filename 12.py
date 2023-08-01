#Q.12) write a program to count the occurence of user-entered words in a sentence

def count_word_occurrences(sentence):
    words = sentence.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

sentence = input("Enter a sentence: ")
user_words = input("Enter words to count: ").split()
occurrences = count_word_occurrences(sentence)
for word in user_words:
    count = occurrences.get(word, 0)
    print(f"{word}: {count}")