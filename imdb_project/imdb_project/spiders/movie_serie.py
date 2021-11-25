import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MovieSerieSpider(CrawlSpider):
    name = 'movie_serie'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= '//td[@class="titleColumn"]/a'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(restrict_xpaths="response.xpath('//td[@class=\"titleColumn\"]/a')"))
        )

    # def start_requests(self):
    #         urls = [
    #             "https://www.imdb.com/chart/top/?ref_=nv_mv_250",
    #             "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
    #         ]
    #         for url in urls:
    #             yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//h1/text()').get()
        item['original_title'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/div/text()').get()
        item['movie_note'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span/text()').get()
        item['genre'] = response.xpath('//li[@data-testid="storyline-genres"]/div/ul/li/a/text()').getall()
        item['date_pub'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[1]/span/text()').get()
        item['movie_runtime'] = response.xpath('//li[@data-testid="title-techspec_runtime"]/div/text()').getall()
        item['public'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[2]/span/text()').get()
        item['synopsis'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[1]/text()').get()
        item['actors'] = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
        item['orginal_language'] = response.xpath('//li[@data-testid="title-details-languages"]/div/ul/li/a/text()').getall()
        item['country_of_origin'] = response.xpath('//li[@data-testid="title-details-origin"]/div/ul/li/a/text()').getall()
        return item
