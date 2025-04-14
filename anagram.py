import random

# List of words for the game

words = ["python", "programming", "developer", "machine", "artificial", "intelligence", "algorithm", "data"]

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

print(scramble_word('python'))