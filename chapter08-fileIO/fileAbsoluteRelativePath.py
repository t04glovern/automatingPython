import os

print(os.path.abspath("."))
print(os.path.abspath(".\\file-working"))
print(os.path.isabs("."))
print(os.path.isabs("\\file-working"))
print(os.path.isabs(os.path.abspath(".")))

print(os.path.relpath("C:\\Windows", "C:\\Users\\Nathan"))
print(os.path.relpath("C:\\Users\\Nathan", "C:\\Windows"))
print(os.getcwd())