# A class for processing html data

# testing


class ProcessHTML:
    def __init__(self, html):
        self.html = html

    def test_page_title(self):
        return self.html.title.get_text()
