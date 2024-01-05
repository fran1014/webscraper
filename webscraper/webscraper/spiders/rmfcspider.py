import scrapy

class RmfcspiderSpider(scrapy.Spider):
    name = "rmfcspider"
    allowed_domains = ["www.realmadrid.com"]
    start_urls = ["https://www.realmadrid.com/es-ES"]

    def parse(self, response):
        # Use CSS selector to select all <p> elements
        paragraphs = response.css('p')
        
        # Iterate over each <p> element and yield its text content
        for p in paragraphs:
            yield {
                'text_content': p.css('::text').get()
            }

        # Extract h1 and h2 from the current page
        h1_text = response.css('h1::text').get()
        h2_text = response.css('h2::text').get()
        
        yield {
            'h1_text': h1_text,
            'h2_text': h2_text
        }

        # Follow links to other pages (e.g., news articles)
        for link in response.css('a::attr(href)').getall():
            if link.startswith('/'):
                # Construct absolute URL if the link is relative
                absolute_url = response.urljoin(link)
                yield response.follow(absolute_url, callback=self.parse_product)

    def parse_product(self, response):
        # Extract h1, h2, and paragraph content from the product page
        h1_text = response.css('h1::text').get()
        h2_text = response.css('h2::text').get()
        paragraphs = response.css('p::text').getall()

        yield {
            'h1_text': h1_text,
            'h2_text': h2_text,
            'paragraphs': paragraphs
        }
