import requests, bs4

# requests.get() to download the main page from the No Starch Press website
res = requests.get('http://nostarch.com')
res.raise_for_status()

# passes the text attribute of the response to bs4.BeautifulSoup()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# BeautifulSoup object that it returns is stored in a variable named noStarchSoup
print(type(noStarchSoup))

# Load html file from disk
exampleFile = open('.\\file-working\\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))

"""
---Examples of CSS Selectors---

soup.select('div')
------------------------
All elements named <div>

soup.select('#author')
------------------------
The element with an  id attribute of author

soup.select('.notice')
------------------------
All elements that use a CSS  class attribute
named notice

soup.select('div span')
------------------------
All elements named <span> that are within an
element named <div>

soup.select('div > span')
------------------------
All elements named <span> that are directly
within an element named <div>, with no other
element in between

soup.select('input[name]')
------------------------
All elements named <input> that have a name
attribute with any value

soup.select('input[type="button"]')
------------------------
All elements named <input> that have an
attribute named type with value  button
"""