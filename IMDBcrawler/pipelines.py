# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import ipdb


class ImdbcrawlerPipeline:
    def process_item(self, item, spider):
        return item


class MoviePipeline:
    def process_item(self, item, spider):
        ipdb.set_trace()
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
