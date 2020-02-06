import requests
import json
from lxml import etree


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1580462552,1580526989; _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWVhNDkxN2FmODlmYmM1M2E3MTRlYmU4MTkyNzY3NjA4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWdEQ1dZdUJCRXFZemg0ajVUeWg3TG1WbC9mU1l1S2lYanhNa1ZqQ2JZSVU9BjsARg%3D%3D--17047fcabaa4c1d40af080695674e0afc5c4e9b3; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1580528477',
    'Host': 'www.xicidaili.com',
    'If-None-Match': 'W/"f207c871b92dfcaad7c9bd6202640318"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
}

type = ['wn','wt','qq']
url_list = ['http://www.xicidaili.com/nn']
for i in type:
    url_list.append('http://www.xicidaili.com/%s'%i)
print(url_list)

req = requests.get('http://www.xicidaili.com/nn',headers = headers)
data = req.content
tree = etree.HTML(data)
list = tree.xpath("//tr[starts-with(@class,*)]//td[position()<6]//text()")
s=[x.strip() for x in list if x.strip()!='']
n=0
data = []
for i in range(int(len(s)/4)):
    IP =s[n]
    port = s[n+1]
    area = s[n+2]
    type = s[n+3]
    n+=4
    data.extend(IP,port,area,type)
print(data)




