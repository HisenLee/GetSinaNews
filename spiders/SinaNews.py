# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from GetSinaNews.items import GetsinanewsItem

class SinanewsSpider(CrawlSpider):
    name = 'SinaNews'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    # http://news.sina.com.cn/c/2018-09-17/doc-ihkahyhx9840920.shtml
    # http://news.sina.com.cn/c/2018-09-16/doc-ifxeuwwr4967916.shtml
    # http://sports.sina.com.cn/basketball/nba/2018-09-17/doc-ifxeuwwr5047758.shtml

    rules = (
        Rule(LinkExtractor(allow=('http:\/\/.*?\.sina\.com\.cn\/.*?[0-9]{4}-[0-9]{2}-[0-9]{2}\/doc-.*?\.shtml'), allow_domains=('sina.com.cn')),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        item = GetsinanewsItem()  # 创建item对象
        item["title"] = response.xpath("/html/head/title/text()").extract()
        item["keyword"] = response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        return item
