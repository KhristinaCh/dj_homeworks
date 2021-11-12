from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=id)
    name = models.TextField()
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField()

