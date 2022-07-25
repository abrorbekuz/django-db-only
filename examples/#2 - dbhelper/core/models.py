from django.db import models

class User(models.Model):
    userId = models.IntegerField()
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name