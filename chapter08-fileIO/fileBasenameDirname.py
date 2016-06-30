import os

path = "C:\\Windows\\System32\\calc.exe"
print(os.path.basename(path))
print(os.path.dirname(path))

# split path into tuple
print(os.path.split(path))

# long way to create tuple
print((os.path.dirname(path), os.path.basename(path)))