"""
Time to practice! Read the link to an article from the input. Print the heading of this article.
"""

import requests

from bs4 import BeautifulSoup

r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
h1 = soup.find_all('h1')
for i in h1:
    print(i.text)
