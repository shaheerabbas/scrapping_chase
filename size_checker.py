import urllib.request

import urllib.parse
url =  "https://hypendium.com/downloads/superbestfriendsplay/Extras/Best%20Friends%20Beat%20Em'%20Ups!/20130625___Best%20Friends%20Beat%20Em'%20Ups%20-%20Dungeons%20&%20Dragons%20Shadow%20over%20Mystara%20(1_2)___I9qYt9FS6qM.jpg"
new_url = urllib.parse.unquote(url)

# print(new_url)
# file = urllib.request.urlopen(url)


# print(file.length)
# from urllib.request import Request, urlopen

# req = Request('https://speed.hetzner.de/100MB.bin', headers={'User-Agent': 'Mozilla/5.0'})
# print(req.head)

# import urllib
# req = urllib.request.Request('https://hypendium.com/downloads/superbestfriendsplay/Extras/Best%20Of/20121231___The%20Best%20of%20Two%20Best%20Friends%20-%20Full%202012%20Compilation!___RjahzsTOUJc.mkv', method='HEAD')
# f = urllib.request.urlopen(req)
# print(f.headers['Content-Length'])

# from urllib.request import urlopen
link = "http://163.172.219.142/mp4/1917.2019.iTALiAN.MD.DVDSCR.XviD-iSTANCE.mp4"
# site = urlopen(new_url)
# meta = site.info()
# print(meta)

import requests
r = requests.head(new_url)
# print(r.headers['Content-Length'])
s = int(r.headers['Content-Length'])
print(r.headers)
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "K", "M", "G")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p)
   return "%s %s" % (s, size_name[i])


size = convert_size(s)
print(size)

mb = s/1000000
print(str(mb) + " MB")
