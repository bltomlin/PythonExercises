"""
O. Henry wrote a lot of interesting short stories, and "The Gift of the Magi" arguably is the most famous . Your task is to print the first paragraph of the story that contains a certain word. The word you are to use is in the first line of the input, and the link to the story is in the second line.
"""

import requests

from bs4 import BeautifulSoup

word = str(input())
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
paragraphs = soup.find_all('p')
for p in paragraphs:
    if p.find(word):
        print(p.text)