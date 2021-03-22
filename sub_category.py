import pandas as pd
from urllib.request import Request, urlopen 
try:
    from bs4 import BeautifulSoup as soup
except ImportError:
    from BeautifulSoup import BeautifulSoup as soup

categories = []
urls = []

my_url = Request('https://chase.pk/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(my_url).read()

page_soup = soup(webpage, "html.parser")
containers = page_soup.findAll("nav", {"id": "left-nav"})
# print(type(containers[0]))

menuLink = containers[0].findAll('a',{'class':'menu-link'})   #Outside categories
# print(len(menuLink))
ul = containers[0].findAll("li",{"class":"item"})   # Inside LI ITEMS
# print(len(ul))
# print(containers[0])

# item = ul[2]
# name = item.a
# print(name.text)

for category in ul:
    name = category.a
    url = category.a['href']
    categories.append(name.text)
    urls.append(url)

# print(categories)
df = pd.DataFrame({'Sub_Category Name':categories, 'URL':urls}) 
df.to_csv('sub_categories.csv', index=False, encoding='utf-8')

