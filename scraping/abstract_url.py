# A class for url
import urllib.request


class AbstractUrl:
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
    headers = {"User-Agent": user_agent}
    data = None

    def __init__(self, url_path):
        self.url_path = url_path

    # TODO: Move this method to a new chanel class.
    # Accepting a partial url path and then completing it feels like potentially dangerous logic.
    def make_chanel_complete_url(self, id):
        modified_url = self.url_path.replace(id.lower(), id)

        return "https://www.chanel.com" + modified_url

    def test_request(self):
        return urllib.request.Request(self.url_path, self.data, self.headers)

    def test_open_url(self, request):
        return urllib.request.urlopen(request)

    def test_get_path(self, response):
        return response.geturl()

    def test_url_error(self):
        with urllib.error.URLError as e:
            print("url lib error", e.reason)
