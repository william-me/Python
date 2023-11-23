#regex findall 
import re

word = "the quick brown fox jumps over the lazy dog"
pattern = r"fox"

search = re.findall(pattern, word)
if search:
    print("Found", search)
else:
    print("Not Found")