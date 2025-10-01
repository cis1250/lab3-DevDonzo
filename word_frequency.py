#!/usr/bin/env python3

import re

# Function provided for sentence validation
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

# Prompt until valid sentence
user_sentence = input("Enter a sentence: ")
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Clean punctuation and normalize
clean_sentence = re.sub(r'[^\w\s]', '', user_sentence).lower()

# Split into words
words = clean_sentence.split()

# Create lists for unique words and their frequencies
unique_words = []
frequencies = []

for word in words:
    if word in unique_words:
        index = unique_words.index(word)
        frequencies[index] += 1
    else:
        unique_words.append(word)
        frequencies.append(1)

# Print word frequencies
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {frequencies[i]}")
