import scrapy
from IMDBcrawler.items import Movie
import re


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
        arr = re.findall(pattern, response.text)
        arr = [x.replace('"const":"', "") for x in arr]
        f = open("test.html", "w")
        f.write(response.text)
