# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MoviesspiderPipeline(object):
    def open_spider(self, spider):
        # 创建数据库连接
        self.connect = pymysql.Connect(host="localhost", user="root", password="root",
                                  database="movies", charset="utf8")
        self.cursor = self.connect.cursor()
        print('打开爬虫',spider)

    def process_item(self, item, spider):
        # 插入数据
        insertSql = "insert into mv_movies(name, img, content, downloadlink, url) VALUE(%s,%s,%s,%s,%s)"
        self.cursor.execute(insertSql,(item['name'],item['img'],item['content'],item['downloadlink'],item['url']))
        self.connect.commit()
        return item

    def close_spider(self,spider):
        # 关闭数据库
        self.cursor.close()
        self.connect.close()
        print('关闭爬虫',spider)