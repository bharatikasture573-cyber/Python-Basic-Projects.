# Import math module
import math
try:
    sentence = input("Enter a sentence: ")
    if sentence.strip() == "":
        raise ValueError("Sentence cannot be empty.")
    words = sentence.split()
    unique_words = set(words)
    print("\nUnique Words (Sorted):")
    for word in sorted(unique_words):
        print(word)

    total_unique = len(unique_words)
    print("\nTotal Unique Words:", total_unique)
    print("Square of Total Unique Words:", math.pow(total_unique, 2))

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)