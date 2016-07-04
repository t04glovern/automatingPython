import zipfile, os

os.chdir('.\\file-working\\delicious')

"""
Extract example.zip to current directory
"""
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()

"""
Extract a specific file to a different location on disk
"""
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extract('spam.txt', '.\\new')
exampleZip.close()
