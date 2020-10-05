from django.core.management.base import BaseCommand, CommandError
from scraping import CreateDesigner


class Command(BaseCommand):
    help = "Add designer by inputting the designer name followed by site url."

    def add_arguments(self, parser):
        parser.add_argument("name", nargs=1, type=str)
        parser.add_argument("url", nargs=1, type=str)

    def handle(self, *args, **options):
        try:
            print(args, options)
            designer = CreateDesigner(options["name"][0], options["url"][0])

            designer.create_designer()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created the designer, {options['name'][0]}."
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR("Opps"))
            self.stdout.write(self.style.ERROR(e))
