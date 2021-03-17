import scrapy
import pandas as pd

lk = pd.read_csv('drama.csv')
half = lk['URL'].values
links = ['https://www.mydramalist.com' + i for i in half]

class reviews(scrapy.Spider):
    name = "reviews"

    def start_requests(self):
        url = links
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse)
    
    def parse(self, response):
        DRAMA_SELECTOR = '//div[contains(@class, "container-fluid title-container")]'
        for reviews in response.xpath(DRAMA_SELECTOR):
        
            TITLE_SELECTOR = './/h1[contains(@class, "film-title")]/a[@title]/text()'
            CHARACTER_SELECTOR = './/div[contains(@class, "p-a-sm")]/ul[contains(@class, "list no-border p-b")]/li[contains(@class, "list-item col-sm-4")][1]/div[contains(@class, "col-xs-8 col-sm-7 p-a-0")]/div[contains(@class, "text-ellipsis")]/small/text()'
            CHARACTER2_SELECTOR = './/div[contains(@class, "p-a-sm")]/ul[contains(@class, "list no-border p-b")]/li[contains(@class, "list-item col-sm-4")][2]/div[contains(@class, "col-xs-8 col-sm-7 p-a-0")]/div[contains(@class, "text-ellipsis")]/small/text()'
            CHARACTER3_SELECTOR = './/div[contains(@class, "p-a-sm")]/ul[contains(@class, "list no-border p-b")]/li[contains(@class, "list-item col-sm-4")][1]/div[contains(@class, "col-xs-8 col-sm-7 p-a-0")]/div[contains(@class, "text-ellipsis")]/small/a/text()'
            CHARACTER4_SELECTOR = './/div[contains(@class, "p-a-sm")]/ul[contains(@class, "list no-border p-b")]/li[contains(@class, "list-item col-sm-4")][2]/div[contains(@class, "col-xs-8 col-sm-7 p-a-0")]/div[contains(@class, "text-ellipsis")]/small/a/text()'

            Title = reviews.xpath(TITLE_SELECTOR).extract_first(),
            Character1 = reviews.xpath(CHARACTER_SELECTOR).extract(),
            Character2 = reviews.xpath(CHARACTER2_SELECTOR).extract(),
            Character3 = reviews.xpath(CHARACTER3_SELECTOR).extract(),
            Character4 = reviews.xpath(CHARACTER4_SELECTOR).extract(),

            for item in zip(Title, Character1, Character2, Character3, Character4):
            #create a dictionary to store the scraped info
                scraped_info = {
                    'Title' : item[0],
                    'Character1' : item[1],
                    'Character2': item[2],
                    'Character3' : item[3],
                    'Character4': item[4],
                }
                yield scraped_info


