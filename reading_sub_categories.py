import csv
import pandas as pd
from urllib.request import Request, urlopen 
from socket import timeout
try:
    from bs4 import BeautifulSoup as soup
except ImportError:
    from BeautifulSoup import BeautifulSoup as soup

count = 203
with open('sub_categories.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    reader.__next__()
    # for row in reader:
    #     print(row[1])
    # print(type(reader))
    for category in reader:
        products = []
        prices = []
        images = []
        barcodes = []
        categories = []
        count += 1
        new_url = category[1]
        # print(new_url)
        url = Request(new_url+'?product_list_limit=all', headers={'User-Agent': 'Mozilla/5.0'})
        # print(url)
        new_webpage = urlopen(url, timeout=100).read()
        page = soup(new_webpage, "html.parser")
        new_page_data = page.findAll("li", {"class": "item product product-item"})
        cat = page.find("h1", {"class" : "page-title"})
        cate = cat.span.text
        print("products for category {}".format(count), len(new_page_data))
        for product in new_page_data:
            print("started fetching record")
            name = product.div.span.img["alt"]
            price = product.find("span", {"class": "price"})
            image = product.div.span.img["src"]

            detail_link = product.div.a["href"]
            detail_url = Request(detail_link, headers={'User-Agent': 'Mozilla/5.0'})
            detail_page = urlopen(detail_url).read()
            detail_soup = soup(detail_page, "html.parser")
            product_info = detail_soup.findAll("div", {"class": "product attribute sku"})
            barcode_with_tag = product_info[1].text
            code = barcode_with_tag.split(':')
            final_code = code[1]



            products.append(name)
            categories.append(cate)
            prices.append(price.text)
            images.append(image)
            barcodes.append(final_code)

        df = pd.DataFrame({'Products':products,'Category':categories ,'Price':prices, 'Image':images, 'Barcode':barcodes}) 
        df.to_csv('category_{}.csv'.format(count), index=False, encoding='utf-8')
