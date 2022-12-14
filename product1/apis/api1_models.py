from django.db import models

class getAllProdect(models.Model):
    
    slug = models.SlugField(blank = True, unique = True)
    title = models.CharField()
    description = models.TextField()
    price = models.FloatField()
    size = models.CharField(max_length= 30)
    quality = models.Choices('high', 'low', 'medium')


    colour = models.CharField('red', 'blue', 'green', 'black')


    image= models.FileField()