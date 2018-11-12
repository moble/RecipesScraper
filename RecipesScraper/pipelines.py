"""
JSON exporter for processed spider items.
"""
import datetime
from scrapy.exporters import JsonItemExporter
import os


class JsonPipeline(object):
  """Save Pipeline output to JSON."""
  def __init__(self, spider_name):
    filename = "output/{}_recipes.json".format(spider_name)
    if not os.path.exists(os.path.dirname(filename)):
      try:
        os.makedirs(os.path.dirname(filename))
      except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
          raise
    self.file = open(filename, 'wb')
    self.file.write(
        '{"date_scraped": "%s", "recipes": ' % datetime.datetime.now()
    )
    self.exporter = JsonItemExporter(self.file, encoding='utf-8',
                                     ensure_ascii=False)
    self.exporter.start_exporting()

  @classmethod
  def from_crawler(cls, crawler):
    return cls(
        spider_name=crawler.spider.name
    )

  def close_spider(self):
    self.exporter.finish_exporting()
    self.file.write("}")
    self.file.close()

  def process_item(self, item):
    self.exporter.export_item(item)
    return item
