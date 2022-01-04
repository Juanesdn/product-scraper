import scrapy
import json
import math
from scrapy.loader import ItemLoader
from ..items import ShopItem


class FalabellaSpider(scrapy.Spider):
    name = 'falabella'
    allowed_domains = ['falabella.com.co']
    next_page = 1
    current_page = 0
    start_urls = [
        f'https://www.falabella.com.co/s/browse/v1/listing/co?page=1&categoryId=cat1361001&categoryName=Computadores--Portatiles-&zone=AFZone']

    def parse(self, response):
        response_dict = json.loads(response.body)

        portatiles = response_dict.get('data').get('results')
        total_items = response_dict.get('data').get('pagination').get('count')
        total_items_per_page = response_dict.get(
            'data').get('pagination').get('perPage')

        # Calcula el total de páginas
        total_pages = math.ceil(total_items / total_items_per_page)

        # Itera por cada portatil y obtiene los datos necesarios
        for portatil in portatiles:
            loader = ItemLoader(
                item=ShopItem(), selector=portatil, response=response)

            loader.add_value("product_url", portatil.get("url"))
            loader.add_value("product_name", portatil.get("displayName"))
            loader.add_value("product_brand", portatil.get("brand"))
            loader.add_value("price",  portatil.get('prices')[
                0].get('price')[0])
            loader.add_value("ref_code", portatil.get("skuId"))
            yield loader.load_item()

        self.next_page += 1  # Aumenta la pagina del siguiente request
        if self.next_page <= total_pages:
            self.current_page += 1
            url = self.change_response_url(response.url)

            # Hace el request a la siguiente página
            yield scrapy.Request(url, callback=self.parse)

    # Cambia el query para la siguiente página
    def change_response_url(self, resUrl):
        return resUrl.replace(
            f'page={self.current_page}', f'page={self.next_page}')
