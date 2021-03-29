import pandas as pd
from urllib.request import Request, urlopen 
from socket import timeout
try:
    from bs4 import BeautifulSoup as soup
except ImportError:
    from BeautifulSoup import BeautifulSoup as soup

import json




def sitemap(url, depth):

    my_url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(my_url).read()

    page_soup = soup(webpage, "html.parser")
    # containers = page_soup.findAll("a",)
    containers = []
    td_container = page_soup.findAll("a",)  
    # info = []
    # dateNtime = td_container[2].next_sibling
    # data = dateNtime.split("    ")
    # print(data)
    # for i in range(len(data)):
    #     if data[i]!="":
    #         info.append(data[i])

    # dt = info[0].split(" ")
    # print(dt)
    for data in td_container[1:]:
        # print(data["href"])
        # print(data.next_sibling)
        info = []
        name = data["href"]
        dateNtime = data.next_sibling
        data = dateNtime.split("    ")
        # print(data)
        for i in range(len(data)):
            if data[i]!="":
                info.append(data[i])

        dt = info[0].split(" ")
        # print(dt)
        date = dt[-2]
        time = dt[-1]
        print(name,date,time)
        
        jsonData = {'name':name, "date":date, "time":time, "url":url+name, "parent_url": "http://localhost:8090/"}
        f = open('nginx_pages/{}.json'.format(name), 'w')
        f.write(json.dumps(jsonData, indent=2))
        f.close()
   


if __name__ == "__main__":

    site = "http://localhost:8090/"
    depth = 0
    sitemap(site, depth)
