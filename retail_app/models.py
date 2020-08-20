from django.db import models

class Business(models.Model):
  name = models.CharField(max_length=50)
  site_url = models.URLField()
  designer = models.ForeignKey(
    'Designer',
    on_delete=models.CASDADE
  )
  category = models.ForeignKey(
    'Category',
    on_delete=models.CASDADE
  )

  def __str__(self):
    return self.name

class Designer(models.Model):
  name = models.CharField(max_length=50)
  site_url = models.URLField()
  category = models.ForeignKey(
    'Category',
    on_delete=models.CASDADE
  )
  product = models.ForeignKey(
    'Product',
    on_delete=models.CASDADE
  )
  collection = models.ForeignKey(
    'Collection',
    on_delete=models.CASDADE
  )
  season = models.ForeignKey(
    'Season',
    on_delete=models.CASDADE
  ) 

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50)
  product = models.ForeignKey(
    'Product',
    on_delete=models.CASDADE
  )

  def __str__(self):
    return self.name

class Product(models.Model):
  product_description = models.ForeignKey(
    'Product_Description',
    on_delete=models.CASDADE
  )
  price = models.ForeignKey(
    'Price',
    on_delete=models.CASDADE
  )
  site_url = models.URLField()
  stock = models.ForeignKey(
    'Stock',
    on_delete=models.CASDADE
  )
  product_details = models.ForeignKey(
    'Product_Details',
    on_delete=models.CASDADE
  )
  CONDITIONS = ('New', ('Preowned', (
    'Like new',
    'Good',
    'Signs of wear',
    'Vintage'
  )))
  condition = models.charField(
    choices=CONDITIONS,
  )
  image = models.ImageField()

  def __str__(self):
    return self.product_description.name

# Should these be models or classes within classes? 
class Product_Description(models.Model):
  name = models.CharField(max_length=200)
  season = models.CharField(max_length=50)
  collection = models.CharField(max_length=50)
  category = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Price(models.model):
  currency = models.CharField(max_length=50)
  amount = models.DecimalField()

  def __str__(self):
    return self.amount

class Stock(models.Model):
  color = models.CharField(max_length=50)
  quantity = models.IntegerField()

  def __str__(self):
    return self.color

class Product_Details(models.Model):
  material = models.TextField()
  size = models.CharField(max_length=50)
  dimensions = models.CharField(max_length=200)
  sku = models.CharField(max_length=50)

  def __str__(self):
    return self.sku

# Not sure if these are actually needed but from a Designer they are many to one,
# But we can understand the collections and seaons through the products as well.
class Collection(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Season(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
