#! /usr/bin/python3
# luckySearch.py - Opens several google search results.

import requests, sys, webbrowser, bs4

print('Googling...')
# download the page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()  # check for possible errors

# Create soup object with downloaded page text
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Get a list of all <a> elements that are within
# an element that has the 'r' CSS class.
# (pattern found by using Inspect Elem in browser)
linkElems = soup.select('.r a')

# opens at least 5 tabs.
n = min(5, len(linkElems))
for i in range(n):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
