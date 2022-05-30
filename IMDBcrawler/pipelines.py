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
