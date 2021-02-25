

import scrapy
from stockscraper.items import StockscraperItem

class StockbotsSpider(scrapy.Spider):
    name = 'stockbots'
    allowed_domains = ['finance.yahoo.com/quote/005930.KS?p=005930.KS&.tsrc=fin-srch']
    start_urls = ['https://finance.yahoo.com/quote/005930.KS?p=005930.KS&.tsrc=fin-srch']

    def parse(self, response):
        Quantity = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/span/text()').extract()
        Price = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()').extract()        
        Low_High_Price = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]/text()').extract()
        title = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1/text()').extract()


        for row in zip(Quantity, Price, Low_High_Price,  title):
            item = StockscraperItem()
            item['Quantity'] = row[0]
            item['Price'] = row[1]
            item['Low_High_Price'] = row[2]
            item['title'] = row[3]                                                

            yield item
