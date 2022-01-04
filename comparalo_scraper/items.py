# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class ShopItem(scrapy.Item):
    product_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    product_name = scrapy.Field(
        output_processor=TakeFirst()
    )
    product_brand = scrapy.Field(
        output_processor=TakeFirst()
    )
    img_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        output_processor=TakeFirst()
    )
    ref_code = scrapy.Field(
        output_processor=TakeFirst()
    )
