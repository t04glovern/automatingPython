import os

for folderName, subfolders, filenames in os.walk('.\\file-working\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('\tSUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('\t\tFILE INSIDE ' + folderName + ': ' + filename)

    print('')