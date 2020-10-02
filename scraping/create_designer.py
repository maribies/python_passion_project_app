from retail_app.models import Designer


class CreateDesigner:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    # TODO: Figure out some validations.
    def create_designer(self):
        return Designer.objects.get_or_create(name=self.name, site_url=self.url)
