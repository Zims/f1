# -*- coding: utf-8 -*-
import scrapy


class F1archiveSpider(scrapy.Spider):
    name = 'f1archive'
    allowed_domains = ['f1.lv']
    start_urls = ['https://f1.lv/2020']

    def parse(self, response):
        for product in response.xpath("//div[@class='td-block-span6']"):
            yield {
                'title': product.xpath(".//div[@class='td_module_1 td_module_wrap td-animation-stack']/h3[@class='entry-title td-module-title']/a/text()").get(),
                'url': product.xpath(".//div[@class='td_module_1 td_module_wrap td-animation-stack']/h3[@class='entry-title td-module-title']/a/@href").get(),

            }