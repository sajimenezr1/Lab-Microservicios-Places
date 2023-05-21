from django.db import models

class Place(models.Model): 
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)