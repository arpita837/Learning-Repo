import re
text = "Python is awesome, python is fun, and Python is powerful."
pattern = r"Python"
matches = re.findall(pattern, text)
print("Occurrences of 'Python':", matches)
