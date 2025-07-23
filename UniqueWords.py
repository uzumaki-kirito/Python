sentence = input("Enter a sentence: ")

words = sentence.split()         # Split sentence into words
unique_words = set(words)        # Convert to set to remove duplicates

print("Unique words:")
for word in unique_words:
    print(word)
