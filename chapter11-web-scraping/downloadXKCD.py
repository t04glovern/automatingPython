#! python3
# downloadXKCD.py - Downloads every single XKCD comic.

import requests, os, bs4, re

first = True        # I am not a smart man

url = 'http://xkcd.com'                 # starting url
os.makedirs('xkcd', exist_ok=True)      # store comics in .xkcd

while not url.endswith('#'):        # the first comic's prev ends with '#'

    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find and download the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Get comic number
        if first:           # I told you I wasn't smart
            first = False
            comicNumber = 'latest'
        else:
            comicNum = re.compile(r'/(\d)(\d)?(\d)?(\d)?')
            cn1 = comicNum.search(url)
            comicNumber = cn1.group(1) + cn1.group(2) + cn1.group(3) + cn1.group(4)

        # Save image to ./kxcd
        imageFile = open(os.path.join('xkcd',  comicNumber + '-' + os.path.basename(comicUrl)), 'wb')
        print(os.path.join('xkcd', os.path.basename(comicUrl)))

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')