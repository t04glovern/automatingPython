import bs4

exampleFile = open('.\\file-working\\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

elems = exampleSoup.select('#author')
print(type(elems))
"""
<class 'list'>
"""
print(len(elems))
"""
1
"""
print(type(elems[0]))
"""
<class 'bs4.element.Tag'>
"""
print(elems[0].getText())
"""
Al Sweigart
"""
print(str(elems[0]))
"""
<span id="author">Al Sweigart</span>
"""
print(elems[0].attrs)
"""
{'id': 'author'}
"""

pElems = exampleSoup.select('p')
print(str(pElems[0]))
"""
<p>Download my <strong>Python</strong> book from <a href="http://
inventwithpython.com">my website</a>.</p>
"""
print(pElems[0].getText())
"""
Download my Python book from my website.
"""
print(str(pElems[1]))
"""
<p class="slogan">Learn Python the easy way!</p>
"""
print(pElems[1].getText())
"""
Learn Python the easy way!
"""
print(str(pElems[2]))
"""
<p>By <span id="author">Al Sweigart</span></p>
"""
print(pElems[2].getText())
"""
By Al Sweigart
"""