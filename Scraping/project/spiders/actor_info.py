import scrapy

class ExtractActor(scrapy.Spider):
    name = "actor"
    start_urls = ['https://www.mydramalist.com/search?adv=titles&ty=68&co=3&ge=19&re=2010,2021&ep=,&rt=6,10&so=popular&page=1']

    def parse(self, response):
        ### This is the first click to visit each kdrama page from the main page with listed kdramas ###
        drama_selector = '//div[@class="col-xs-9 row-cell content"]'
        for kdrama in response.xpath(drama_selector):
            follow_drama = kdrama.xpath('.//h6[@class="text-primary title"]/a/@href').extract_first()
            drama_link = 'https://www.mydramalist.com' + follow_drama
            yield response.follow(url=drama_link, callback=self.parse_kdrama_page)
            
        next_page = response.xpath('.//li[@class="page-item next"]/a[@class="page-link"]/@href').extract_first()
        if next_page is not None:
            next_url = 'https://www.mydramalist.com' + next_page
            yield response.follow(url = next_url, callback=self.parse)

    def parse_kdrama_page(self, response):
        ### We are inside the kdrama page! Let's get some details about the kdrama ###
        title = response.xpath('.//ul[@class="list m-b-0"]/li/span[@itemprop="name"]/text()').extract_first()
        main_selector = '//li[@class="list-item col-sm-4"]'
        for info in response.xpath(main_selector):
            actor_name = info.xpath('.//div[@class="col-xs-8 col-sm-7 p-a-0"]/a[@href]/b[@itempropx="name"]/text()').extract_first()
            char_name = info.xpath('.//div[@class="text-ellipsis"]/small/text()').extract_first()
            if char_name is None:
                char_name = info.xpath('.//div[@class="text-ellipsis"]/small/a/text()').extract_first()
            role = info.xpath('.//div[@class="col-xs-8 col-sm-7 p-a-0"]/small[@class="text-muted"]/text()').extract_first()
            actor_url = info.xpath('.//div[@class="col-xs-4 col-sm-5 p-r p-l-0"]/a/@href').extract_first()
            actor_link = 'https://www.mydramalist.com' + actor_url
            request = scrapy.Request(url=actor_link, callback=self.parse_actor_info, cb_kwargs=dict(Title=title, ActorName=actor_name, CharName=char_name, Role=role))
            request.cb_kwargs['foo'] = 'bar'  # add more arguments for the callback
            yield request

    def parse_actor_info(self, response, Title, ActorName, CharName, Role, foo):
        ### This is the second click where we are inside the indiv actor page ###
        gender = response.xpath('.//ul[@class="list m-b-0"]/li[contains(text(), " Male")]').extract_first()
        if gender is not None:
            gender = 'Male'
        else:
            gender = 'Female'
        image = response.xpath('.//div[@class="col-sm-4 text-center cover hidden-md-up"]/img[@class="img-responsive inline"]/@src').extract_first()
        yield dict(
            Title = Title, 
            CharName = CharName, 
            Role = Role, 
            ActorName = ActorName,
            Gender = gender,
            Image = image,
        )