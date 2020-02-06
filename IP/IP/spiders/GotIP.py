# -*- coding: utf-8 -*-
import scrapy
from IP.items import IpItem

class GotipSpider(scrapy.Spider):
    name = 'GotIP'
    allowed_domains = ['www.xicidaili.com']
    start_urls = []
    type = ['nn','wn','wt','qq']
    for i in type:
        for j in range(1,5):
            start_urls.append('http://www.xicidaili.com/%s/%d'%(i,j))
    print(start_urls)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url,callback=self.parse,meta={'proxy':'http://49.84.132.141:8118'})


    def parse(self, response):
        list = response.xpath("//tr[starts-with(@class,*)]//td[position()<6]//text()").extract()
        s = [x.strip() for x in list if x.strip() != '']
        n = 0
        item = IpItem()
        for i in range(int(len(s) / 4)):
            IP = s[n]
            port = s[n + 1]
            area = s[n + 2]
            type = s[n + 3]
            item['IP'] = IP.strip()
            item['port'] =port.strip()
            item['area'] = area.strip()
            item['type'] = type.strip()
            n += 4
            yield item



