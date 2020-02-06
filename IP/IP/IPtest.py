import requests

proxies={
    'http':'http://49.84.132.141:8118'
}

url = 'http://ip.filefab.com/index.php'
req = requests.get(url,proxies=proxies)
data = req.text
print(data)