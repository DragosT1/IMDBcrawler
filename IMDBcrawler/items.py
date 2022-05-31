# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Movie(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    date_of_scraping = scrapy.Field()
    directors = scrapy.Field()
    title = scrapy.Field()
    poster_img = scrapy.Field()
    rating = scrapy.Field()
    release_year = scrapy.Field()
    top_cast = scrapy.Field()
    url = scrapy.Field()
    uid = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


class Actor(scrapy.Item):
    name = scrapy.Field()
    uid = scrapy.Field()


class ActorsAndMovies(scrapy.Item):
    actor_uid = scrapy.Field()
    movie_uid = scrapy.Field()
