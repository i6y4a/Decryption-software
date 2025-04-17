import random
import string
import math

def generate_substitution(alphabet):
    substituted_alphabet = list(alphabet)
    random.shuffle(substituted_alphabet)
    return ''.join(substituted_alphabet)

def encrypt_word(word, substitution):
    alphabet = string.ascii_lowercase
    encrypted_word = ''.join(substitution[alphabet.index(char)] if char in alphabet else char for char in word)
    return encrypted_word

def start(word):
    word = word.lower()
    alphabet = string.ascii_lowercase

    total_possibilities = math.factorial(len(alphabet))
    print(f"Total number of possible monoalphabetic substitutions: {total_possibilities}")

    seen_substitutions = set()
    possibilities = []

    while len(possibilities) < 1000:
        substitution = generate_substitution(alphabet)
        if substitution not in seen_substitutions:
            seen_substitutions.add(substitution)
            encrypted_word = encrypt_word(word, substitution)
            possibilities.append(encrypted_word)

    print("\nThese are 1000 possibilities to encrypt the text:")
    for i, possibility in enumerate(possibilities, start=1):
        print(f"{i}: {possibility}")

if __name__ == "__main__":
    start("Ali")
