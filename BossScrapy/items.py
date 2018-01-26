# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossscrapyItem(scrapy.Item):
    # //公司名称
    companyName = scrapy.Field()
    # 公司人数
    companyPeoNum = scrapy.Field()
    # 工作年限
    workYear = scrapy.Field()
    # 文凭
    dioloma = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 发布时间
    relTime = scrapy.Field()

