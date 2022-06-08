"""
Your task is to find and print a subtitle of the article by an index. You are given two input values:

The first one is the index of the subtitle. It starts from 0 in Python. You do not need to subtract one from the given number.
The second one is the the link to the article.
The subtitles are stored in the <h2> tag. For example, your code should print The Definite Article for the following input:

1
https://www.grammarly.com/blog/articles/
"""

import requests

from bs4 import BeautifulSoup

index = int(input())
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
all_subtitle = soup.find_all('h2')
count = 0
for i in all_subtitle:
    if count == index:
        print(i.text)
    count += 1