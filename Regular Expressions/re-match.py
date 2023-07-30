import re
text = "Hello, World!"
pattern = r"Hello"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")
