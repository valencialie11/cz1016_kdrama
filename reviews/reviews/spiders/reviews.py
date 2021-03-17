import scrapy
import pandas as pd

lk = pd.read_csv('kdramaclean.csv')
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
            RATINGS_SELECTOR = './/div[contains(@class, "hfs")]/b[contains(@itempropx, "ratingValue")]/text()'
            RANKED_SELECTOR = './/ul[contains(@class, "list m-a-0 hidden-md-up")]/li[contains(@class, "list-item p-a-0")][9]/text()'
            POPULARITY_SELECTOR = './/ul[contains(@class, "list m-a-0 hidden-md-up")]/li[contains(@class, "list-item p-a-0")][10]/text()'
            ACTOR1_SELECTOR = './/div[contains(@class, "p-a-sm")]/ul[contains(@class, "list no-border p-b")]/li[contains(@class, "list-item col-sm-4")][1]/div[contains(@class, "col-xs-8 col-sm-7 p-a-0")]/a[@href]/b[contains(@itempropx, "name")]/text()'
            URL1_SELECTOR = './/div[contains(@class, "p-a-sm")]/ul[contains(@class, "list no-border p-b")]/li[contains(@class, "list-item col-sm-4")][1]/div[contains(@class, "col-xs-4 col-sm-5 p-r p-l-0")]/a/@href'
            ACTOR2_SELECTOR = './/div[contains(@class, "p-a-sm")]/ul[contains(@class, "list no-border p-b")]/li[contains(@class, "list-item col-sm-4")][2]/div[contains(@class, "col-xs-8 col-sm-7 p-a-0")]/a[@href]/b[contains(@itempropx, "name")]/text()'
            URL2_SELECTOR = './/div[contains(@class, "p-a-sm")]/ul[contains(@class, "list no-border p-b")]/li[contains(@class, "list-item col-sm-4")][2]/div[contains(@class, "col-xs-4 col-sm-5 p-r p-l-0")]/a/@href'

            Title= reviews.xpath(TITLE_SELECTOR).extract_first(),
            Ratings = reviews.xpath(RATINGS_SELECTOR).extract_first(),
            Ranked = reviews.xpath(RANKED_SELECTOR).extract(),
            Popularity = reviews.xpath(POPULARITY_SELECTOR).extract(),
            Actor1 = reviews.xpath(ACTOR1_SELECTOR).extract(),
            URL1 = reviews.xpath(URL1_SELECTOR).extract_first(),
            Actor2= reviews.xpath(ACTOR2_SELECTOR).extract(),
            URL2 = reviews.xpath(URL2_SELECTOR).extract_first(),

            for item in zip(Title, Ratings, Ranked, Popularity, Actor1, URL1, Actor2, URL2):
            #create a dictionary to store the scraped info
                scraped_info = {
                    'Title' : item[0],
                    'Ratings' : item[1],
                    'Ranked': item[2],
                    'Popularity': item[3],
                    'Actor 1' : item[4],
                    'URL 1': item[5],
                    'Actor 2' : item[6],
                    'URL 2': item[7]
                }
                yield scraped_info

