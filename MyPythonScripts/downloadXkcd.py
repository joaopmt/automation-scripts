#! /usr/bin/python3
# downloadXkcd.py - Downloads every single XKCD comic from http://xkcd.com

import requests, os, bs4, time

url = 'http://xkcd.com'
# create dir to store imgs if it doesnt already exists
os.makedirs('xkcd', exist_ok=True)

startTime = time.time()
while not url.endswith('#'):  # (the first page's url ends with '#')
    # Download the page.
    print('Downloading page', url, '...')
    page = requests.get(url)
    page.raise_for_status()
    # Create soup obj.
    soup = bs4.BeautifulSoup(page.text)
    # get a list of <img> elems that is inside a id attribute 'comic'
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image.')
    else:
        try:
            # get the content from 'src' tag, which is a link to img
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image', comicUrl, '...')
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
print('Elapsed time:', (time.time() - startTime))
            
