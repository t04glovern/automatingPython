import zipfile, os

os.chdir('.\\file-working\\delicious')

exampleZip = zipfile.ZipFile('example.zip')

print(exampleZip.namelist())
"""
Print contents of Zip
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
"""

spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
"""
Print the filesize of spam.txt within the zip
13908
"""

print(spamInfo.compress_size)
"""
Print the filesize of spam.txt after compression
3828
"""

print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
"""
Print the compression ratio
"""

exampleZip.close()
"""
Close the zip file
"""