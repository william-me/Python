#split() function splits the string where the pattern matches and returns a list of strings where the splits have occurred.
import re

text = "apple, banana, cherry, orange"
pattern = r",\s"

split_result = re.split(pattern, text)
print("Split result: ", split_result)  # ['apple', ' banana', ' cherry', ' orange']