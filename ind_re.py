import scrapy
import pandas as pd

lk = pd.read_csv('url.csv')
half = lk['URL'].values
links = ['https://mydramalist.com/' + i + '/reviews?xlang=en-US&status=completed' for i in half]
counter = 1
class kdrama(scrapy.Spider):
    name = "drama"
    start_urls = [links[0]]
    
    def parse(self, response):
        global counter
        title = response.xpath('//h1[@class="film-title"]/a/@title')
        title_ext = title.extract()

        reviews = response.xpath('//div[contains(@id,"review")]/div[2]/div/div')
        for review in reviews:
            exception = review.xpath('.//p/text()').extract()
            if len(exception)==0:
                raw = review.xpath('./text()').extract()
            else:
                raw = exception
            re = [sen.replace('\r\n', ' ') for sen in raw]
            review_ext = [' '.join([para.strip() for para in re if not para.isspace()])]
            yield {'title': title_ext,
                   'review': review_ext}
            
        NEXT_PAGE_SELECTOR = '//li[@class = "page-item next"]/a[@class= "page-link"]/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = 'http://www.mydramalist.com' + next_href
            yield scrapy.Request(url=next_page_url, dont_filter=True)
        elif counter < len(links):
            yield scrapy.Request(url=links[counter], dont_filter=True)
            counter += 1
