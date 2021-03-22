import pandas as pd
from urllib.request import Request, urlopen 
from socket import timeout
try:
    from bs4 import BeautifulSoup as soup
except ImportError:
    from BeautifulSoup import BeautifulSoup as soup

categories = []

my_url = Request('https://chase.pk/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(my_url).read()

page_soup = soup(webpage, "html.parser")
containers = page_soup.findAll("nav", {"id": "left-nav"})
# print(type(containers[0]))

menuLink = containers[0].findAll('a',{'class':'menu-link'})   #Outside categories
print(len(menuLink))
ul = containers[0].findAll("li",{"class":"item"})   # Inside LI ITEMS
# print(ul)
# print(containers[0])

# item = menuLink[1]
# name = item.span
# print(name.text)




count = 0
for category in menuLink:
    products = []
    prices = []
    count += 1
    print("Started processing for category{}".format(count))
    new_url = category['href']
    url = Request(new_url+'?product_list_limit=all', headers={'User-Agent': 'Mozilla/5.0'})
    new_webpage = urlopen(url, timeout=100).read().decode('utf-8')
    page = soup(new_webpage, "html.parser")
    new_page_data = page.findAll("li", {"class": "item product product-item"})
    print("products for category {}".format(count), len(new_page_data))
    for product in new_page_data:
        print("Fetching products")
        name = product.div.span.img["alt"]
        price = product.find("span", {"class": "price"})
        products.append(name)
        prices.append(price.text)

    df = pd.DataFrame({'Products':products, 'Price':prices}) 
    df.to_csv('category_{}.csv'.format(count), index=False, encoding='utf-8')



# new
# u = menuLink[10]
# new_url = u['href']
# print(new_url+'?product_list_limit=all')

# url = Request(new_url+'?product_list_limit=all', headers={'User-Agent': 'Mozilla/5.0'})
# new_webpage = urlopen(url).read()
# page = soup(new_webpage, "html.parser")
# new_page_data = page.findAll("li", {"class": "item product product-item"})
# print(len(new_page_data))

# data = new_page_data[1]
# name = data.div.span.img["alt"]
# print(name)
###############
# for category in menuLink:
#     name = category.span
#     categories.append(name.text)


# df = pd.DataFrame({'Category Name':categories}) 
# df.to_csv('parent_categories.csv', index=False, encoding='utf-8')

