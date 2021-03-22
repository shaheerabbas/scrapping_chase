import pandas as pd
from urllib.request import Request, urlopen 
try:
    from bs4 import BeautifulSoup as soup
except ImportError:
    from BeautifulSoup import BeautifulSoup as soup

products = []
prices = []
images = []
categories_list = []

my_url = Request('https://chase.pk/edible-grocery/dry-grocery/egg.html?product_list_limit=all', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(my_url).read()

page_soup = soup(webpage, "html.parser")
containers = page_soup.findAll("li", {"class": "item product product-item"})

categories = page_soup.findAll("div", {"class" : "category-image"})
category = categories[0]
# print(category.img["alt"])

# print("length",len(containers))

container = containers[0]
print(container.div.span.img["alt"])

detail_link = container.div.a["href"]

new_url = Request(detail_link, headers={'User-Agent': 'Mozilla/5.0'})
detail_page = urlopen(new_url).read()

detail_soup = soup(detail_page, "html.parser")
product_info = detail_soup.findAll("div", {"class": "product attribute sku"})
# print(len(product_info))
barcode_with_tag = product_info[1].text
code = barcode_with_tag.split(':')
final_code = code[1]
print(final_code)
# price = container.find("span", {"class": "price"})
# print(price.text)

# for container in containers:
#     name = container.div.span.img["alt"]
#     image = container.div.span.img["src"]
#     price = container.find("span", {"class": "price"})
#     products.append(name)
#     images.append(image)
#     prices.append(price.text)
#     categories_list.append(category.img["alt"])


# df = pd.DataFrame({'Product Name':products, 'Category': categories_list,'Price':prices, 'Images':images}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')

