'''
防止dns污染自动匹配被DNS污染但是ip没有被屏蔽的网站
'''
import requests
import re
from fake_useragent import UserAgent
ua = UserAgent()
headers = {"User-Agent": ua.random,}
count=0
try:
    file =open("domain.txt")
except:
    file = {input("DOMIN:")}
for i in file:
    r = requests.get("https://en.ipip.net/dns.php?a=dig&host="+i+"&area%5B%5D=north_america&area%5B%5D=south_america",headers=headers)
    res = re.findall("\d+\.\d+\.\d+\.\d+",r.text)
    print(res)
    for j in res:
        try:
            ip = requests.get("http://"+j)
        except:
            continue
        print(j+" "+i)
        count+=1
        if(count == 1):
            count=0
            break
            
