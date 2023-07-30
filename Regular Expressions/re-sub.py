import re
text = "Hello, world! Hello, everyone! Hello, Python!"
pattern = r"Hello"
new_text = re.sub(pattern, "Hi", text)
print(new_text)
