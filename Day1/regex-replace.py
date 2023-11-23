#replacement of a string using the sub() function
import re

word = "the quick brown fox jumps over the lazy dog"
pattern = r"brown"
replacement = "white"

new_word = re.sub(pattern, replacement, word)
print("New word: ", new_word)