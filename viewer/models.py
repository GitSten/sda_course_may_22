from django.db import models

# Create your models here.


class Genre(models.Model):
    '''
    with the help of the Django ORM this will be translated to a database table
    '''
    name = models.CharField(max_length=128)
