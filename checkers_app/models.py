from django.db import models

# Create your models here.

class User(models.Model):
    title       = models.TextField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(default='add something!')
    featured    = models.BooleanField()


class UserMoves(models.Model):
    name = models.CharField(max_length=120)
    moves = models.CharField(max_length=120)
    
