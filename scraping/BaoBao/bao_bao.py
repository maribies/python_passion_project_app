from scraping import (
    BaoBaoHtml,
    BaoBaoProductBuilder,
    BaoBaoProductDocument,
    BaoBaoProducts,
)


class BaoBao:
    def create_products(self, products_urls):
        if products_urls == [] or products_urls is None:
            raise Exception("No products urls.")

        # Get html per product.
        for url in products_urls:
            html = BaoBaoHtml(url)

            document = BaoBaoProductDocument(html.get_html_data(url))

            builder = BaoBaoProductBuilder(document, {"url": url})

            # Create product.
            builder.create_all_product_information()

        return len(products_urls)
