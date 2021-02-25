# import scrapy
# from stockscraper.items import StockscraperItem

# def remove_space(price:list) -> list:
#     result = []
#     for i in range(len(price)):
#         if len(price[i].strip()) >0:
#             result.append(price[i].strip())
#     return result
    
# class StockbotsSpider(scrapy.Spider):
#     name = 'stockbots'
#     allowed_domains = ['paxnet.co.kr']
#     start_urls = ['http://www.paxnet.co.kr/stock/analysis/presentValue?abbrSymbol=005930']

#     def parse(self, response):
#         # title = response.xpath('//*[@id="gnbHtml"]/div[1]/div/div[1]/div[2]/div[1]/h1/span/text()').extract()        
#         title = response.css('.title::text').extract()
#         quantity = response.xpath('//*[@id="Low_High_Price"]/div[1]/div[2]/div[1]/div/table/tbody/tr[4]/td[1]/text()').extract()
#         price = response.xpath('//*[@id="Low_High_Price"]/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]/span/text()').extract()        
#         low_price = response.xpath('//*[@id="Low_High_Price"]/div[1]/div[2]/div[1]/div/table/tbody/tr[3]/td[2]/text()').extract()
#         high_price = response.xpath('//*[@id="Low_High_Price"]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/td[2]/text()').extract()

#         converted_price =  remove_space(price)

#         for row in zip(title,quantity, converted_price, low_price, high_price):
#             item = StockscraperItem()
#             item['title'] = row[0]              
#             item['quantity'] = row[1]
#             item['price'] = row[2]
#             item['low_price'] = row[3]
#             item['high_price'] = row[4]            
                                            

#             yield item

import scrapy
from stockscraper.items import StockscraperItem

# def converted_price(Low_High_Price:list) -> list:
#     result = []
#     result = (str(Low_High_Price).split('-'))
#     return result
    

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