
# checks spelling of the given words to the closest match

import difflib

words = ["hello", "world", "python", "programming", "beautiful",
         "friend", "computer", "school", "learning", "project",
         "correct", "spell", "language", "student"]

text = input("Enter a word: ").lower()

if text in words:
    print("Spelling is correct!")
else:
    suggestion = difflib.get_close_matches(text, words, n=1)

    if suggestion:
        print("Did you mean:", suggestion[0])
    else:
        print("No suggestion found.")
