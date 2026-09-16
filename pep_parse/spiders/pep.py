import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    DOMAIN = 'peps.python.org'

    allowed_domains = [DOMAIN]
    start_urls = [f'https://{DOMAIN}/']

    def parse(self, response):
        for pep_row in response.css("table.pep-zero-table tbody tr"):
            tds = pep_row.css("td")

            data = {
                "number": tds[1].css("::text").get().strip(),
                "name": tds[2].css("::text").get().strip(),
            }

            yield response.follow(
                tds[1].css("a::attr(href)").get(),
                callback=self.parse_pep,
                meta={"data": data},
            )

    def parse_pep(self, response):
        status = (
            response.xpath(
                '//dt[contains(., "Status")]/following-sibling::dd[1]//text()'
            )
            .get()
            .strip()
        )
        data = response.meta["data"]

        yield PepParseItem(
            number=data["number"], name=data["name"], status=status
        )
