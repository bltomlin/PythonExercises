"""
Read a link from the input. Get all text paragraphs from all the a tags and single out the topic titles (not any word or phrase!) starting with the letter S. Print the final list. Beware of empty lines.

For example, for this input and letter L (here we provide the link to the archive for consistency's sake):

http://web.archive.org/web/20201201053628/https://www.who.int/health-topics

the output should be:

["Landslides", "Lassa fever", "Leishmaniasis", "Leprosy", "Lymphatic filariasis"]

The link in the test will be the same one.
"""

import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()
count = 0
thislist = []
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
paragraphs = soup.find_all('a')
for p in paragraphs:
    text = p.text
    if (paragraphs.get('href')).find('topics') and len(text) > 1 and (paragraphs.get('href')).find('entity'):
        thislist.append(text)
print(thislist)
