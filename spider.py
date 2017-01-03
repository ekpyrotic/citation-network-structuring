class MySpider(scrapy.Spider):
    name = 'researchpapers'
    #allowed_domains = ['example.com']
    start_urls = [
        'http://genomebiology.biomedcentral.com/articles/10.1186/gb-2009-10-3-r25',
    ]

    def parse(self, response):
        for h3 in response.xpath('//h3').extract():
            yield {"title": h3}

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)
            