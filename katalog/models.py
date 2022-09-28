from django.db import models
#sudah ada di template
class CatalogItem(models.Model): 
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField() #64-bit integer
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()