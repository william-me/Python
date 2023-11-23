#checks for a match at the beginning of the string
import re

word = "the quick brown fox jumps over the lazy dog"
pattern = r"quick"

match = re.match(pattern, word)
if match:
    print("Matched", match.group())
else:
    print("Not matched")