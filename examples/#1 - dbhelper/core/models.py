from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=64)
    count = models.IntegerField()
    
    def __str__(self):
        return self.name