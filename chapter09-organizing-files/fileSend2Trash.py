import send2trash

baconFile = open('.\\file-working\\bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('.\\file-working\\bacon.txt')

# Note that the send2trash() function can only send files to the recycle bin;
# it cannot pull files out of it.