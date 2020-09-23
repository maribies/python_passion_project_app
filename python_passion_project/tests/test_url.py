from django.test import TestCase
import urllib.request


class UrlTest(TestCase):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
    headers = {"User-Agent": user_agent}
    data = None

    def setUp(self):
        self.url_path = "https://www.chanel.com/us/fashion/p/AS2215B0458694305/mini-flap-bag-with-handle-velvet-strass-gold-tone-metal/quickview"

    def request(self, url_path):
        return urllib.request.Request(url_path, self.data, self.headers)

    def open_url(self, request):
        return urllib.request.urlopen(request)

    def get_path(self, response):
        return response.geturl()

    def url_error(self):
        with urllib.error.URLError as e:
            print("url lib error", e.reason)
