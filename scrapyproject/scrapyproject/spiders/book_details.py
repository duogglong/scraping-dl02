import scrapy


class BookDetailsSpider(scrapy.Spider):
    name = "book-details"
    
    def start_requests(self):
        URL = 'https://books.toscrape.com/'
        # URL = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('article.product_pod'):
            title = selector.css('h3 > a::attr(title)').get()
            price = selector.css('.price_color::text').get()
            # Access the details page
            detail_url = selector.css('h3 > a::attr(href)').get()
            
            # Access details page, send meta in page inside
            yield response.follow(detail_url, self.parse_detail, meta={'title': title, 'price': price})
        next_page_link = response.css('li.next a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)
        
    def parse_detail(self, response):
        # Get data from metaData
        title = response.meta['title']
        price = response.meta['price']

        # Get desc in detail page
        description = response.css('div#product_description + p::text').get()

        # Return details info
        yield {
            'title': title,
            'price': price,
            'description': description
        }