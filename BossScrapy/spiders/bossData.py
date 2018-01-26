import scrapy
from BossScrapy.items import BossscrapyItem


class bossDataSpider(scrapy.Spider):
    name = "BossData"
    start_urls = (
     'https://www.zhipin.com/c101280600/h_101280600/?query=android&page=1&ka=page-1/',
    )
    def parse(self, response):
        # print("获取到的值", response.body)
        item = BossscrapyItem()
        selector = scrapy.Selector(response)
        job_list = selector.xpath('//div[@class="job-list"]//li')
        for eachJob in job_list:
            companyName = eachJob.xpath('.//div[@class="company-text"]//a/text()').extract()
            peoNum = eachJob.xpath('.//div[@class="company-text"]/p/text()[3]').extract()
            worYear = eachJob.xpath('.//div[@class="info-primary"]/p/text()[2]').extract()
            dioloma = eachJob.xpath('.//div[@class="info-primary"]/p/text()[3]').extract()
            salary = eachJob.xpath('.//span[@class ="red"]/text()').extract()
            relTime = eachJob.xpath('.//div[@class="info-publis"]/p/text()').extract()
            item['companyName'] = companyName
            item['companyPeoNum']= peoNum
            item['workYear'] = worYear
            item['dioloma'] = dioloma
            item['salary'] = salary
            item['relTime'] = relTime
            yield item
        nextPage = selector.xpath('//div[@class="page"]//a[@class="next"]/@href').extract()
        next_page='https://www.zhipin.com'+nextPage[0]
        print("获取下一页", next_page)
        yield scrapy.Request(next_page,callback=self.parse)
