import shelve

"""" --- Shelve Save --- """

"""
To read and write data using the  shelve module, you first import  shelve .
Call  shelve.open() and pass it a filename, and then store the returned shelf
value in a variable
"""
shelfFile = shelve.open(".\\file-working\mydata")

cats = ["Zophie", "Pooka", "Simon"]

"""
When you’re done, call  close() on the shelf value. Here, our shelf
value is stored in shelfFile. We create a list  cats and write
shelfFile['cats'] = cats to store the list in  shelfFile as a value
associated with the key 'cats' (like in a dictionary).
"""
shelfFile["cats"] = cats
"""
Then we call  close() on shelfFile
"""
shelfFile.close()

"""" --- Shelve Load --- """

"""
We open the shelf files to check that our data was stored correctly
"""
shelfFile = shelve.open(".\\file-working\mydata")
print(type(shelfFile))
"""
Entering  shelfFile['cats'] returns the same list that we stored earlier, so we
know that the list is correctly stored, and we call  close()
"""
print(shelfFile["cats"])
shelfFile.close()

"""" --- Shelve Keys and Values --- """

shelfFile = shelve.open(".\\file-working\mydata")

"""
shelf values have  keys() and  values() methods that
will return list-like values of the keys and values in the shelf. Since these
methods return list-like values instead of true lists, you should pass them
to the  list() function to get them in list form
"""
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()