import os

helloFile = open(".\\file-working\hello.txt")
helloContent = helloFile.read()
print(helloContent)

# 'r' can be used to specify this is a read operation
sonnetFile = open(".\\file-working\sonnet29.txt", 'r')
sonnetContent = sonnetFile.read()
print(sonnetContent)

# Note you have to re-instantiate the file.open() operation
# else your previous read operation will be used with the
# cursor at the end of the file
sonnetFile = open(".\\file-working\sonnet29.txt")
sonnetContentLines = sonnetFile.readlines()
print(sonnetContentLines)