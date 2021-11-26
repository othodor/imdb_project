import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SerieCrawlSpider(CrawlSpider):
    name = 'serie_crawl'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= '//td[@class="titleColumn"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//h1/text()').get()
        item['original title'] = response.xpath('//div[@data-testid="hero-title-block__original-title"]/text()').get()
        item['serie note'] = response.xpath('//span[@class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]/text()').get()
        item['genre'] = response.xpath('//li[@data-testid="storyline-genres"]/div/ul/li/a/text()').getall()
        item['Seasons'] = response.xpath('//select[@id="browse-episodes-season"]/option/text()').get()
        item['Episodes'] = response.xpath('//h3[@class="ipc-title__text"]/span[@class="ipc-title__subtext"]/text()').get()
        item['date_pub'] = response.xpath('//ul[@data-testid="hero-title-block__metadata"]/li[2]/a/text()').get()
        item['movie_runtime'] = response.xpath('//li[@data-testid="title-techspec_runtime"]/div/text()').getall()
        item['public'] = response.xpath('//ul[@data-testid="hero-title-block__metadata"]/li[3]/a/text()').get()
        item['synopsis'] = response.xpath('//div[@data-testid="storyline-plot-summary"]/div/div/text()').get()
        item['actors'] = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
        item['orginal_language'] = response.xpath('//li[@data-testid="title-details-languages"]/div/ul/li/a/text()').getall()
        item['country_of_origin'] = response.xpath('//li[@data-testid="title-details-origin"]/div/ul/li/a/text()').getall()
        return item
