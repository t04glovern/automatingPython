import os

baconFile = open(".\\file-working\\bacon.txt", "w")
baconFile.write("Hello Bacon!\n")
baconFile.close()

baconFile = open(".\\file-working\\bacon.txt", "a") # append mode
baconFile.write("Bacon is not a vegetable.")
baconFile.close()

baconFile = open(".\\file-working\\bacon.txt")
content = baconFile.read()
baconFile.close
print(content)