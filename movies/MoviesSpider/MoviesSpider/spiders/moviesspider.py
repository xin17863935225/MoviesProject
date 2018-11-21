# -*- coding: utf-8 -*-
import scrapy
from ..items import MoviesspiderItem

class MoviesspiderSpider(scrapy.Spider):
    name = 'moviesspider'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/dyzz/index.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        # print(response.body.decode('GBK'))
        movies = response.xpath('//div[@class="co_content8"]/ul/td/table')
        # print(movies)
        for movie in movies:
            item = MoviesspiderItem()
            url = movie.xpath('.//tr[2]/td[2]/b/a/@href').get()
            item['url'] = 'https://www.dytt8.net'+url
            # print(item)
            yield scrapy.Request(item['url'], callback=self.parse_mv,dont_filter=True,meta={'item': item})

        # 下一页
        next_page = response.xpath('//div[@class="co_content8"]/div[@class="x"]/td/a[text()="下一页"]')
        if next_page:

            next_page_url = next_page.xpath('.//@href').get()
            print(next_page_url)
            yield response.follow(next_page_url)


    def parse_mv(self, response):
        # 获取传的参数
        item = response.meta['item']
        # 电影名
        item['name'] = response.xpath('//div[@class="title_all"]/h1/font/text()').get().strip()
        # 内容介绍
        content = response.xpath('string(//td/p)').get().strip()
        content = content.split('【')[0]
        content = content.split('◎')
        item['content'] = '\n◎'.join(content)
        # 下载链接
        item['downloadlink'] = response.xpath('//a[contains(@href,"magnet")]/@href').get().strip()
        # 图片链接
        item['img'] = response.xpath('//p/img[@border="0"][1]/@src').get().strip()
        print(item)
        yield item
