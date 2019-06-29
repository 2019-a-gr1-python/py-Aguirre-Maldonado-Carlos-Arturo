import pandas as pd
import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedor = response.css('article.product_pod')

        titulos = etiqueta_contenedor.css('h3 > a::attr(title)').extract()

        stocks = etiqueta_contenedor.css('div.product_price > p.instock.availability::text').extract()

        precios = etiqueta_contenedor.css('div.product_price > p.price_color::text').extract()

        stocks = stocks[1::2]

        stocks=list(map(lambda x:x.strip(),stocks))

        resultados_crawl = {
            'titulos': titulos,
            'stocks' : stocks,
            'precios': precios
        }

        df = pd.DataFrame(resultados_crawl, columns=['stocks','precios' ], index =titulos)

        print(df)

        df.to_json('./resultados.json')
        df.to_pickle('./resultados.pickle')

