#!/usr/bin/env python

from itertools import product
from string import ascii_uppercase
import re

ciphertext = "LUSSJMC JB LMVWJ GO DTJJTKJZ YRYDNY"
original_spaces = [i for i, char in enumerate(ciphertext) if char == " "]  # Record space positions
ciphertext_clean = ciphertext.replace(" ", "").replace(",", "").replace("'", "").replace(".", "").replace("’", "").upper()  # Remove spaces and special characters and convert to uppercase

# Frequency of letters in English (from most to least common)
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

# List of common English words for scoring
common_words = {"THE", "AND", "THIS", "THAT", "HAVE", "WITH", "FOR", "ARE", "IS", "IN"}


# Function to shift letters according to a key
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char in ascii_uppercase:
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Function to add spaces back to the plaintext
def add_spaces(plaintext, space_positions):
    for pos in space_positions:
        plaintext = plaintext[:pos] + " " + plaintext[pos:]
    return plaintext

# Function to score plaintext based on English letter frequency and common words
def score_plaintext(plaintext):
    score = 0
    # Score based on letter frequency
    for char in plaintext:
        if char in english_freq:
            score += (26 - english_freq.index(char))  
    # Score based on common words (only standalone words)
    for word in common_words:
        
        if re.search(r'\b' + re.escape(word) + r'\b', plaintext):
            score += 100  
    return score

# Store all results with their scores
results = []

for key_length in range(1, 5):
    print(f"Trying key length: {key_length}")
    for key in product(ascii_uppercase, repeat=key_length):
        key = ''.join(key)
        plaintext = vigenere_decrypt(ciphertext_clean, key)
        plaintext_with_spaces = add_spaces(plaintext, original_spaces)  # Add spaces back
        score = score_plaintext(plaintext_with_spaces)
        results.append((key, plaintext_with_spaces, score))

# Sort results by score in descending order
results.sort(key=lambda x: x[2], reverse=True)

# Print the top 200 results
print("\nTop 200 Results:")
for i, (key, plaintext, score) in enumerate(results[:200]):
    print(f"Rank {i+1}: Key: {key}, Plaintext: {plaintext}, Score: {score}")