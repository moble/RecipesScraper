"""
Recipe item pulled from each recipe.
"""
import scrapy
from scrapy import Item
from scrapy.loader.processors import MapCompose

from RecipesScraper.utils import remove_extra_whitespace


class RecipeItem(Item):
  """Info from recipe to be collected."""
  totalTime = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  nutrition = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  name = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  author = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  url = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  image = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  recipeIngredient = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  aggregateRating = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  recipeYield = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  recipeInstructions = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  video = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  mainEntityOfPage = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  cookTime = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  recipeCategory = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  review = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  prepTime = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  description = scrapy.Field(input_processor=MapCompose(remove_extra_whitespace))
  # recipe_name = scrapy.Field(
  #     input_processor=MapCompose(remove_extra_whitespace)
  # )
  # ingredients = scrapy.Field(
  #     input_process=MapCompose(remove_extra_whitespace)
  # )
  # tags = scrapy.Field(
  #     input_process=MapCompose(remove_extra_whitespace)
  # )
  # url = scrapy.Field(
  #     input_process=MapCompose(remove_extra_whitespace)
  # )
  # description = scrapy.Field(
  #     input_process=MapCompose(remove_extra_whitespace)
  # )
