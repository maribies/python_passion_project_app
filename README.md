# Find And Seek - A python passion project

Find And Seek is a Python passion project completed to gain competency in Python and object oriented design and development. It brings together a passion for retail- specifically luxury retail- and technology.

This project was developed with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to scrape websites for the luxury products and details, then built with [Django](https://docs.djangoproject.com/en/3.1/).

## Development

Some things to note to get started locally-

This project uses [pipenv](https://docs.pipenv.org/) to simplify environment variables and dependencies.

To Run the interactive shell-
```
pipenv shell
```

## Usage

Scraping/Getting data-
```
python manage.py getinitialdata -all
```
This command will scrape and initiate new classes for the business, designer, and site. (The flag can be updated for just the individual classes needed.)


Running the local server-
```
python manage.py runserver
```

## Production

[Heroku](https://devcenter.heroku.com/) is used to serve and deploy the production app.

To check out the latest production version of the app, it is currently found at [https://murmuring-reaches-12951.herokuapp.com/](https://murmuring-reaches-12951.herokuapp.com/). (Refined Heroku deployment coming soon!)


## Contributing
As this is a passion project for now, reviews and learning opportunities are appreciated in terms of contributions.

## License
[MIT](https://choosealicense.com/licenses/mit/)
