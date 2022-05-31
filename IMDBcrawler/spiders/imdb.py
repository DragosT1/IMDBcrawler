import scrapy
from IMDBcrawler.items import Movie
import re
from datetime import date
import json


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/user/ur24609396/watchlist"]

    custom_settings = {
        "ITEM_PIPELINES": {
            "IMDBcrawler.pipelines.MoviePipeline": 300,
        }
    }

    def parse(self, response):
        items = response.xpath("//script[contains(., 'starbars')]/text()")
        txt = items.get()
        pattern = re.compile(r"[^t]const.{3}tt\d{7}")
        import ipdb

        # ipdb.set_trace()
        arr = re.findall(pattern, txt)
        arr = [x.replace('"const":"', "https://www.imdb.com/title/") for x in arr]
        # f = open("test1.txt", "w")
        # f.write(str(arr))
        print(arr)
        print(len(arr))

        for link in arr:
            yield scrapy.Request(link, callback=self.parse_movie)

    def parse_movie(self, response):
        movie_items = response.xpath("//*[@id='__next']/main/div/section[1]")
        for movie in movie_items:
            movie = Movie()

            movie["category"] = response.xpath(
                "//div[@class='sc-16ede01-8 hXeKyz sc-910a7330-11 GYbFb']//li[@class='ipc-inline-list__item ipc-chip__text']/text()"
            ).getall()

            movie["date_of_scraping"] = str(date.today())

            movie["directors"] = response.xpath(
                "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()"
            ).getall()

            movie["title"] = response.xpath(
                "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1/text()"
            ).getall()
            print(movie["title"])
