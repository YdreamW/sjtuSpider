# -*- coding: utf-8 -*-
import scrapy


class WmySpider(scrapy.Spider):
    name = 'wmy'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print(response)
