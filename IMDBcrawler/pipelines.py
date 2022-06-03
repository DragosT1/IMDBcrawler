# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import ipdb
import json
from IMDBcrawler.items import Movie
from IMDBcrawler.items import Actor
from IMDBcrawler.items import ActorsAndMovies
import sqlite3
import sys


class ImdbcrawlerPipeline:
    def process_item(self, item, spider):
        return item


class MoviePipeline:
    def process_item(self, item, spider):
        # ipdb.set_trace()
        return item


class SimpleStoragePipeline:
    def open_spider(self, spider):
        self.movie = open("imdb_movie.json", "w")
        self.actor = open("imdb_actor.json", "w")
        # open 1 file for each type
        # connect to db

    def process_item(self, item, spider):
        # if type of item = Movie insert into movie
        if isinstance(item, Movie):
            line = json.dumps(ItemAdapter(item).asdict()) + "\n"
            self.movie.write(line)
            return item
        elif isinstance(item, Actor):
            line = json.dumps(ItemAdapter(item).asdict()) + "\n"
            self.actor.write(line)
            return item

    def close_spider(self, spider):
        self.movie.close()
        self.actor.close()


class SqlitePipeline:
    def open_spider(self, spider):

        # Create/connect to db
        self.con = sqlite3.connect("imdbScraper.db")

        # Create cursor
        self.cur = self.con.cursor()

        self.create_movies_table()

    def create_movies_table(self):
        # Drop MOVIES if exists
        self.cur.execute("""DROP TABLE IF EXISTS movies""")

        # Create MOVIES table if none exists
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS movies(
            category TEXT,
            date_of_scraping TEXT,
            directors TEXT,
            rating TEXT,
            release_year TEXT,
            title TEXT,
            top_cast TEXT,
            url TEXT,
            image_urls TEXT)
        """
        )

    def process_item(self, item, spider):

        if isinstance(item, Movie):
            self.cur.executemany(
                """INSERT INTO movies (category,date_of_scraping,directors,rating,release_year,title,top_cast,url,image_urls) VALUES (?,?,?,?,?,?,?,?,?)""",
                [
                    (
                        json.dumps(item["category"]),
                        json.dumps(item["date_of_scraping"]),
                        json.dumps(item["directors"]),
                        json.dumps(item["rating"]),
                        json.dumps(item["release_year"]),
                        json.dumps(item["title"]),
                        json.dumps(item["top_cast"]),
                        json.dumps(item["url"]),
                        json.dumps(item["image_urls"]),
                    )
                ],
            )
        self.con.commit()

        return item


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

# from itemadapter import ItemAdapter
# import json
# from imdbC.items import Movie, Actor, ActorsAndMovies, ActorFilmography
# class ImdbcPipeline:
#     def process_item(self, item, spider):
#         return item
# class SimpleStoragePipeline:
#     def open_spider(self, spider):
#         self.movie = open("imdb_movie.json", "w")
#         self.actor = open("imdb_actor.json", "w")
#         # open 1 file for each type
#         # connect to db
#     def process_item(self, item, spider):
#         # if type of item = Movie insert into movie
#         if isinstance(item, Movie):
#             line = json.dumps(ItemAdapter(item).asdict()) + "\n"
#             self.movie.write(line)
#             return item
#         elif isinstance(item, Actor):
#             line = json.dumps(ItemAdapter(item).asdict()) + "\n"
#             self.actor.write(line)
#             return item
#     def close_spider(self, spider):
#         self.movie.close()
#         self.actor.close()
