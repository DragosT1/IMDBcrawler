import scrapy
from IMDBcrawler.items import Movie
from IMDBcrawler.items import Actor
from IMDBcrawler.items import ActorsAndMovies
import re
from datetime import date
import json
import ipdb


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["www.imdb.com", "m.media-amazon.com"]
    start_urls = ["https://www.imdb.com/user/ur24609396/watchlist"]

    custom_settings = {
        "ITEM_PIPELINES": {
            "IMDBcrawler.pipelines.MoviePipeline": 300,
            "scrapy.pipelines.images.ImagesPipeline": 299,
        },
        "IMAGES_STORE": "images",
    }

    def parse(self, response):
        items = response.xpath("//script[contains(., 'starbars')]/text()")
        txt = items.get()
        pattern = re.compile(r"[^t]const.{3}tt\d{7}")

        arr = re.findall(pattern, txt)
        arr = [x.replace('"const":"', "https://www.imdb.com/title/") for x in arr]
        # f = open("test1.txt", "w")
        # f.write(str(arr))
        # print(arr)
        # print(len(arr))

        for link in arr[:5]:
            yield scrapy.Request(link, callback=self.parse_movie)

    def parse_movie(self, response):
        # movie_items = response.xpath("//*[@id='__next']/main/div/section[1]")
        # for movie in movie_items:
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
        ).getall()[0]
        # print(movie["title"])

        # ipdb.set_trace()

        movie["image_urls"] = [
            "https://m.media-amazon.com/images/M/MV5BODQxYWM2ODItYjE4ZC00YzAxLTljZDQtMjRjMmE0ZGMwYzZjXkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_QL75_UY562_CR21,0,380,562_.jpg"
        ]

        movie["rating"] = response.xpath(
            "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()"
        ).get()

        movie["release_year"] = response.xpath(
            "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div/ul/li[1]/span/text()"
        ).get()

        movie["top_cast"] = response.xpath("//div[@class='sc-18baf029-7 eVsQmt']//a/text()").getall()

        movie["url"] = response.url

        movie["uid"] = movie["url"][-10:-1]

        yield movie

        pattern = re.compile(r"characters.{1}nm\d{7}")
        arr = re.findall(pattern, response.text)
        actor_url_set = set([x.replace("characters/", "https://www.imdb.com/name/") for x in arr])
        for link in actor_url_set:
            yield scrapy.Request(url=link, callback=self.parse_actor)

    # def parse_actor(self, response):
    #     actor_items = response.xpath("//*[@id='content-2-wide']")
    #     actor = Actor()
    #     actor["name"] = response.xpath("//h1/span[@class='itemprop']/text()").get()
    #     uid = response.url
    #     actor["uid"] = uid[26 : len(uid) - 1]
    #     actor["filmography_movie_url"] = response.xpath(
    #         "//div[@class='filmo-category-section']/div[contains(@id,'act')]/b/a/@href"
    #     ).getall()
    #     # [x = ("https://www.imdb.com/title" + x) for x in arr]
    #     # actor["filmography_movie_url"] = arr
    #     actor["filmography_movie_title"] = response.xpath(
    #         "//div[@class='filmo-category-section']/div[contains(@id,'act')]/b/a/text()"
    #     ).getall()
    #     yield actor
