#search for a pattern in a string
import re

word = "the quick brown fox jumped over the lazy dog"
pattern = r"brown"

search = re.search(pattern, word)
if search:
    print("Found:", search.group())  # Found brown
else:
    print("Nothing  found")