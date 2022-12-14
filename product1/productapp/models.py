from django.db import models

# Create your models here.
class productMainModel(models.Model):
    
    slug = models.SlugField(blank = True, unique = True)
    title = models.CharField()
    description = models.TextField()
    price = models.FloatField()
    size = models.CharField(max_length= 30)
    quality = models.Choices()

class productColorModel(models.Model):

    Product = models.ForeignKey(productMainModel)
    colour = models.CharField()

class productImageModel(models.Model):

    Product = models.ForeignKey(productMainModel)
    image= models.FileField()



