# Find And Seek - A python passion project

Find And Seek is a Python passion project completed to gain competency in Python and object oriented design and development. It brings together a passion for retail- specifically luxury retail- and technology.

This project was developed with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to scrape websites for the luxury products and details, then built with [Django](https://docs.djangoproject.com/en/3.1/). The database is [PostgreSQL](https://www.postgresql.org/docs/13/index.html) and deployed through [Heroku](https://devcenter.heroku.com/).

Coming soon- mobile version with React Native.

## Development
Some things to note to get started locally-

This project uses [pipenv](https://docs.pipenv.org/) to simplify environment variables and dependencies.

To Run the interactive shell-
```
pipenv shell
```

### Testing
To run tests, start shell and enter:
```
python manage.py test
```

For a coverage report:
```
coverage report -i
```

[VCR.py](https://vcrpy.readthedocs.io/en/latest/usage.html) was added for testing to record the tests.
To update VCR:
For a coverage report:
```
python manage.py gettestdata
```

## Usage
Scraping/Getting data-
Scraping commands are now based off of individual designers' sites, of which there are currently 2.
Bao Bao by Issey Miyake:
```
python manage.py getbaobaoproducts
```
Chanel:
```
python manage.py getchanelproducts
```

This command will scrape and initiate new classes for the products. (The flag can be updated for just the individual classes needed.)


Running the local server (with coverage)-
```
coverage run manage.py runserver
```
or 
```
python manage.py runserver
```

## Production
To check out the latest production version of the app, it is currently found at [https://findandseek.herokuapp.com/](https://findandseek.herokuapp.com/).


## Contributing
As this is a passion project for now, reviews and learning opportunities are appreciated in terms of contributions.

## License
[MIT](https://choosealicense.com/licenses/mit/)
