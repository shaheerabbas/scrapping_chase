import pandas as pd
from urllib.request import Request, urlopen 
from socket import timeout
try:
    from bs4 import BeautifulSoup as soup
except ImportError:
    from BeautifulSoup import BeautifulSoup as soup

import json




def sitemap(url, depth):
    movies_name = []
    
   
    my_url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(my_url).read()

    page_soup = soup(webpage, "html.parser")
    # containers = page_soup.findAll("a",)
    containers = []
    td_container = page_soup.findAll("td",)  
    # print(len(td_container))
    # td = div_container[1]
    # print(td)

    for td in td_container:
        if td.a and not td.a["href"].startswith('/'):
            containers.append(td.a)

    # print(containers)
    details = page_soup.findAll("td",{"align": "right"})
    date_time_details = details[1::2]
    sizes = details[2::2]
    # print(depth, len(date_time_details))

    ################################################################################################### hello

    if depth >=2:
        movies_dateTime = []
        for date_time in date_time_details:
            # print(date_time.text)
            
            dateTime = date_time.text
            # print(dateTime)
            movies_dateTime.append(dateTime)

        # print(movies_dateTime)


    for data in containers:
        if data["href"].endswith('/'):
            new_url = url + data["href"]
            print(new_url)
            sitemap(new_url, depth+1)
        else:
            # i=0
            name = data.text
            movies_name.append(name)
            
            # print(name)
            # print(name, movies_dateTime[i])
            # print(i)
            # i+=1

    for i in range(len(movies_name)):
        n = movies_name[i]
        # dt = movies_dateTime[i]
        # print(n, dt)
        pageDateTime = movies_dateTime[i]
        dateNTime = pageDateTime.split(" ")
        date = dateNTime[0]
        time = dateNTime[1]

        jsonData = {'name':n, "date":date, "time":time, "url":url+n, "parent_url": "https://hypendium.com/downloads/superbestfriendsplay/"}

        f = open('sitemap_pages/{}.json'.format(n), 'w')
        f.write(json.dumps(jsonData, indent=2))
        f.close()




if __name__ == "__main__":

    site = " https://hypendium.com/downloads/superbestfriendsplay/"
    depth = 0
    sitemap(site, depth)
