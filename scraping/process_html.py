class ProcessHTML:
    def __init__(self, html):
        self.html = html

    def page_title(self):
        page_title = self.html.title.get_text()

        return page_title.rstrip("| CHANEL")
