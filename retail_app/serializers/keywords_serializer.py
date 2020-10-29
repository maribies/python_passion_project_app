from retail_app.models import SearchProductKeywords
import json


class KeywordsSerializer:
    def __init__(self, search: SearchProductKeywords):
        self.keywords = search.keywords

    def for_json(self):
        return self.keywords
