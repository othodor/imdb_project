from typing import Text
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MovieSerieSpiderSpider(scrapy.Spider):
    name = 'movie_serie_spider'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    # def start_requests(self):
    #     yield scrapy.Request(url='')

    # rules = (
    #    Rule(LinkExtractor(restrict_xpaths="//h3")),
    #    Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    # def parse(self, response):
    #     all_titles = response.xpath('//td[@class="titleColumn"]/')

    def parse_item(self, response):
        all_movies_titles = response.xpath('//td[@class="titleColumn"]/')
        # print(len(all_movies_titles))
        for movie in all_movies_titles:
            title = movie.xpath('.//a/text()').extract_first()
            film_date = movie.xpath('.//span[@class="secondaryInfo"]/text()').extract_first()
            url_movie = self.allowed_domains[0] + movie.xpath('.//a/@href').extract_first()
        yield {
            "Titre": title,
            "Date": film_date,
            "Film URL": url_movie
        }
        # print(response.url)
       
       
       
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
