import pprint, os

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

fileObj = open("myCats.py", "w")
fileObj.write("cats = " + pprint.pformat(cats) + "\n")
fileObj.close()

"""
since Python scripts are themselves just text files with the .py file
extension, your Python programs can even generate other Python programs
"""
import myCats

print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])