import re


# 12) Write a Python program that matches a word containing 'z'
def text_match(text):
    patterns = '\w*z.\w*'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))