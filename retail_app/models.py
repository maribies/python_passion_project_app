from django.db import models

class Business(models.Model):
  name = models.CharField(max_length=50)
  site_url = models.URLField()
  designer = models.ForeignKey(
    'Business_Designer',
    on_delete=models.CASCADE
  )
  category = models.ForeignKey(
    'Category',
    on_delete=models.CASCADE
  )

  class Meta:
    verbose_name_plural = "Businesses"

  def __str__(self):
    return self.name

class Business_Designer(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = "Business Designers"

class Designer(models.Model):
  name = models.CharField(max_length=50)
  site_url = models.URLField()

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.name

class Product(models.Model):
  designer = models.CharField(max_length=100)
  product_description = models.ForeignKey(
    'Product_Description',
    on_delete=models.CASCADE
  )
  product_price = models.ForeignKey(
    'Product_Price',
    on_delete=models.CASCADE
  )
  site_url = models.URLField()
  stock = models.ForeignKey(
    'Product_Stock',
    on_delete=models.CASCADE
  )
  product_details = models.ForeignKey(
    'Product_Details',
    on_delete=models.CASCADE
  )
  CONDITIONS = [
    (1, 'New'), 
    (2, 'Preowned')
  ]
  condition = models.CharField(
    choices=CONDITIONS,
    max_length=15
  )
  image = models.ForeignKey(
    'Product_Image',
    on_delete=models.CASCADE
  )

  def __str__(self):
    return self.product_description.name

class Product_Description(models.Model):
  name = models.CharField(max_length=200)
  season = models.CharField(max_length=50)
  collection = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  brand = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = "Product Description"

class Product_Price(models.Model):
  currency = models.CharField(max_length=50)
  amount = models.DecimalField(max_digits=19, decimal_places=2,)

  class Meta:
    verbose_name_plural = "Product Prices"

  def __str__(self):
    return self.currency + str(self.amount)

class Product_Stock(models.Model):
  colors = models.ForeignKey(
    'Product_Color',
    on_delete=models.CASCADE
  )
  quantities = models.ForeignKey(
    'Product_Quantity',
    on_delete=models.CASCADE
  )
  
  class Meta:
    verbose_name_plural = "Product Stock"

  def __str__(self):
    return str(self.colors) + ' - ' + str(self.quantities) + ' units '

class Product_Color(models.Model):
  color = models.CharField(max_length=50)

  def __str__(self):
    return self.color

class Product_Quantity(models.Model):
  quantity = models.IntegerField(null=True, blank=True, default=None)

  def __str__(self):
    return str(self.quantity)

class Product_Details(models.Model):
  material = models.TextField()
  size = models.CharField(max_length=50)
  dimensions = models.CharField(max_length=200)
  sku = models.CharField(max_length=50)

  class Meta:
    verbose_name_plural = "Product Details"

  def __str__(self):
    return self.material + ' - ' + self.size  + ' - ' + self.dimensions  + ' - ' + self.sku

class Collection(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Season(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

#TODO: Add names for better description in admin.
class Product_Image(models.Model):
  image = models.ImageField()

  def _str_(self):
    return self.image

  class Meta:
    verbose_name_plural = "Product Images"
