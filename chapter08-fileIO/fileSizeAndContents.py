import os

# You'll need to run this one as admin

path = "C:\\Windows\\System32\\calc.exe"
print(os.path.getsize(path))
print(os.listdir("C:\\Windows\\System32"))

totalSize = 0
for filename in os.listdir("C:\\Windows\\System32"):
    totalSize = totalSize + os.path.getsize(os.path.join("C:\\Windows\\System32", filename))

print(totalSize)