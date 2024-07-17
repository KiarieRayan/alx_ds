import re

# text = 'The quick brown fox jumps over 12 lazy dogs.'

# #{4,} is a greedy match
# print(re.findall(r"\b\w{4,}\b",text))

# #find 'o' followed by one ot more 'g's
# print(re.findall(r"og+", text))

text_one = 'abc123'
#regex pattern w a capturing one or more digit
patterns = r'(\d+)'
#searching the text for the pattern
match = re.search(patterns, text_one)
#checking if a match is found.
if match:
    #retrieve the first captured group
    captured_group = match.group(1)
    print("Captured Group:", captured_group)
else:
    print("No match is found")