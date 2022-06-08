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