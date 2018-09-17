# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetsinanewsItem(scrapy.Item):
    # 存储网页标题
    title = scrapy.Field()
    # 存储网页关键词
    keyword = scrapy.Field()
    pass
