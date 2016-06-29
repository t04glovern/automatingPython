spam = "Hello World!"

print(spam.islower())
print(spam.isupper())
print("HELLO".isupper())
print("12345abc".islower())
print("12456".isupper())

# isalpha() returns True if the string consists only of letters and is not blank.
print(spam.isalpha())
print("HelloWorld".isalpha())

# isalnum() returns True if the string consists only of letters and numbers and is not blank
print(spam.isalnum())
print("HelloWorld1245".isalnum())

# isdecimal() returns True if the string consists only of numeric characters and is not blank.
print(spam.isdecimal())
print("12345".isdecimal())

# isspace() returns True if the string consists only of spaces, tabs, and new- lines and is not blank
print(spam.isspace())
print("     \t".isspace())

# istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
print(spam.istitle())
print("hello world!".istitle())