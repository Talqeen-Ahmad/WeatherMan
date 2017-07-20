import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = [
        'https://www.goodreads.com/quotes/'
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'Quotes': quote.xpath('.//div[@class="quoteText"]/text()').extract_first(),
                'Author': quote.xpath('.//a[@class="authorOrTitle"]/text()').extract_first(),
                
            }

        for href in response.xpath('//a[@class="next_page"]/@href'):
		yield response.follow(href,self.parse)
        
            
