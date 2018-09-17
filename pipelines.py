# -*- coding: utf-8 -*-

import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class GetsinanewsPipeline(object):

    # 初始化的时候直接连接本地对应的数据库
    def __init__(self):
        self.conn = pymysql.connect(host = "127.0.0.1", user = "root", password = "root", database = "sinanews")

    # 接收字段数据并存入数据库表
    def process_item(self, item, spider):
        title = item["title"][0]
        keyword = item["keyword"][0]
        sql = "insert into news(title, keyword) values ('" + title + "', '" + keyword + "');"
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.conn.close()