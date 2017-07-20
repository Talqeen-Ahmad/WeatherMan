import scrapy
from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "laptop_spider"
    start_urls = [
        'http://www.mega.pk/laptop/'
    ]

    def parse(self, response):
	item = TutorialItem()
	for laptop in response.xpath('//li[@class="col-xs-6 col-sm-4 col-md-4 col-lg-3"]'):
            	
                item["Laptop_Name"] = laptop.xpath('.//div[@id="lap_name_div"]/h3/a/text()').extract_first()
		item["Detail"] = laptop.xpath('.//ul[@class="detailer"]/li/text()').extract()
		item["Price"] = laptop.xpath('.//div[@class="cat_price"]/text()').extract()
		yield item
		              
           
	for href in response.xpath('//div[@class="pagination"]/a/@href'):
		yield response.follow(href,self.parse)
        
            
	
