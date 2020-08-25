#TODO: The business name and site_url will always be static.
##### The business name could be dynamic by input to also return url and not populate everything.
##### Designers and product categories should also be dynamically scraped and updated.
Businesses = {
    'Bao Bao': { 
      'name': 'Bao Bao by Issey Miyake',
      'site_url': 'https://www.shopbaobaoisseymiyake.com/',
      'designers': ['Issey Miyake'],
      'categories': ['Bags']
    }
}

def get_business(input):
    return Businesses[input]

def main(input):
    return get_business(input)

if __name__ == '__main__':
    main(input)
