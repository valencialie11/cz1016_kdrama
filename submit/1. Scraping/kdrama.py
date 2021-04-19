import scrapy

class kdrama(scrapy.Spider):
    name = "kdrama"
    start_urls = ['https://www.mydramalist.com/search?adv=titles&ty=68&co=3&ge=19&re=2010,2021&ep=,&rt=6,10&so=popular&page=1']
    
    def parse(self, response):
        DRAMALIST_SELECTOR = '//div[@class="col-xs-9 row-cell content"]'
        for kdrama in response.xpath(DRAMALIST_SELECTOR):
        
            TITLE_SELECTOR = './/h6[contains(@class, "text-primary title")]/a[@href]/text()'
            INFO_SELECTOR = './/span[contains(@class, "text-muted")]/text()'
            RATINGS_SELECTOR = './/span[contains(@class, "p-l-xs score")]/text()'
            URL_SELECTOR = './/h6[contains(@class, "text-primary title")]/a[@href]'

            Title= kdrama.xpath(TITLE_SELECTOR).extract_first(),
            Info= kdrama.xpath(INFO_SELECTOR).extract_first(),
            Ratings= kdrama.xpath(RATINGS_SELECTOR).extract_first(),
            URL= kdrama.xpath(URL_SELECTOR).extract()
                #we just want the first element that matches the selector. This gives us a string, rather than a list of elements.
                
            for item in zip(Title, Info, Ratings, URL):
            #create a dictionary to store the scraped info
                scraped_info = {
                    'Title' : item[0],
                    'Info' : item[1],
                    'Ratings' : item[2],
                    'URL' : item[3]
                }

            #yield or give the scraped info to scrapy
                yield scraped_info


            NEXT_PAGE_SELECTOR = './/li[@class = "page-item next"]/a[@class= "page-link"]/@href'
            next_page = response.xpath(NEXT_PAGE_SELECTOR).extract()
            if next_page:
                next_href = next_page[0]
                next_page_url = 'http://www.mydramalist.com' + next_href
                request = scrapy.Request(url=next_page_url)
                yield request

