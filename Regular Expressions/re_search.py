import re
text = "Hello, this is a sample text with some numbers: 12345 and 67890."
pattern = r"\d+"  # Matches one or more digits
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")
