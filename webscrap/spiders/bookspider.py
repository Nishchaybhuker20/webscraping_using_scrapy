import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        book =  response.css('article.product_pod')

        for firstbook in book:
            relative_url = firstbook.css('h3 a ::attr(href)').get()

            if 'catalogue/' is relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url

            yield response.follow(book_url, callback=self.parse_book_page)
                

        if next_page is not None:
            if 'catalogue/' is next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page

            yield response.follow(next_page_url, callback=self.parse)


    def parse_book_page(self, response):
        table_rows = response.css("table tr")

        yield {
            'url' : response.url,
            'title' : response.css('.product_main h1::text').get(),
            'product_type'  : table_rows[1].css('td::text').get(),
            'price_excl_tax'  : table_rows[2].css('td::text').get(),
            'price_incl_tax'  : table_rows[3].css('td::text').get(),
            'tax'  : table_rows[4].css('td::text').get(),
            'availability'  : table_rows[5].css('td::text').get(),
            'num_reviews'  : table_rows[6].css('td::text').get(),
            'stars' : response.css('p.star-rating').attrib['class'],


        }