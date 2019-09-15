# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem


class Soft5566Spider(scrapy.Spider):
    name = 'soft5566'
    allowed_domains = ['soft5566.com']
    # start_urls = ['http://www.soft5566.com/down/41245-1.html']
    start_urls = ['http://www.soft5566.com/down/']

    def start_requests(self):
        url_ = 'http://www.soft5566.com/down/'
        for n in range(2901,58001):
            url = url_ + str(n) + '-1.html'
            yield scrapy.Request(url, callback=self.parse, meta={'game_id': str(n)})

    def parse(self, response):
        item = MyspiderItem()
        item['game_title'] = response.xpath('//li[@class="gameID_cn"]/text()').extract()[0]
        item['game_id'] = response.meta['game_id']
        yield item
