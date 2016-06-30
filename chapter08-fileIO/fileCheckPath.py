import os

print(os.path.exists("C:\\Windows"))
print(os.path.exists("C:\\Cows"))

print(os.path.isdir("C:\\Windows\\System32"))
print(os.path.isdir("C:\\Windows\\System32\\calc.exe"))

print(os.path.isfile("C:\\Windows\\System32"))
print(os.path.isfile("C:\\Windows\\System32\\calc.exe"))