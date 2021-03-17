import scrapy
import pandas as pd

reviews = pd.read_csv('reviewscleanbfr.csv')

url1 = []

for i in range(0,1150):
    url1.insert(i, reviews['URL 1'][i])

url2 = []

for i in range(0,1150):
    url2.insert(i, reviews['URL 2'][i])

url1.extend(url2)

class info(scrapy.Spider):
    name = "info"

    def start_requests(self):
        for link in url1:
            yield scrapy.Request(url=link, callback=self.parse)
    
    def parse(self, response):
        ACTOR_SELECTOR = '//div[contains(@class, "content-side hidden-sm-down")]'
        for info in response.xpath(ACTOR_SELECTOR):
        
            NAME_SELECTOR = './/div[contains(@class, "box-header p-b-0 text-center")]/h1[contains(@class, "film-title m-b-0")]/text()'
            INFO_SELECTOR = './/ul[contains(@class, "list m-b-0")]/li[contains(@class, "list-item p-a-0")][2]/text()'
            INFO1_SELECTOR = './/ul[contains(@class, "list m-b-0")]/li[contains(@class, "list-item p-a-0")][3]/text()'
            INFO2_SELECTOR = './/ul[contains(@class, "list m-b-0")]/li[contains(@class, "list-item p-a-0")][4]/text()'
            INFO3_SELECTOR = './/ul[contains(@class, "list m-b-0")]/li[contains(@class, "list-item p-a-0")][5]/text()'
            INFO4_SELECTOR = './/ul[contains(@class, "list m-b-0")]/li[contains(@class, "list-item p-a-0")][6]/text()'
            INFO5_SELECTOR = './/ul[contains(@class, "list m-b-0")]/li[contains(@class, "list-item p-a-0")][7]/text()'
            INFO6_SELECTOR = './/ul[contains(@class, "list m-b-0")]/li[contains(@class, "list-item p-a-0")][8]/text()'
            IMAGE_SELECTOR = '//div[contains(@class, "col-sm-4 text-center cover hidden-md-up")]/img[contains(@class, "img-responsive inline")]/@src'
            

            Name = info.xpath(NAME_SELECTOR).extract_first(),
            Info = info.xpath(INFO_SELECTOR).extract_first(),
            Info1 = info.xpath(INFO1_SELECTOR).extract_first(),
            Info2 = info.xpath(INFO2_SELECTOR).extract_first(),
            Info3 = info.xpath(INFO3_SELECTOR).extract_first(),
            Info4 = info.xpath(INFO4_SELECTOR).extract_first(),
            Info5 = info.xpath(INFO5_SELECTOR).extract_first(),
            Info6 = info.xpath(INFO6_SELECTOR).extract_first(),
            Image = info.xpath(IMAGE_SELECTOR).extract()

            for item in zip(Name, Info, Info1, Info2, Info3, Info4, Info5, Info6, Image):
            #create a dictionary to store the scraped info
                scraped_info = {
                    'Name' : item[0],
                    'Info' : item[1],
                    'Info1' : item[2],
                    'Info2' : item[3],
                    'Info3': item[4],
                    'Info4': item[5],
                    'Info5': item[6],
                    'Info6': item[7],
                    'Image': item[8]
                }
                yield scraped_info

