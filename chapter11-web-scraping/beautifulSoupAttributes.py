import bs4

soup = bs4.BeautifulSoup(open('.\\file-working\\example.html'), 'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
"""
<span id="author">Al Sweigart</span>
"""
print(spanElem.get('id'))
"""
author
"""
print(spanElem.get('some_nonexistent_addr') == None)
"""
True
"""
print(spanElem.attrs)
"""
{'id': 'author'}
"""