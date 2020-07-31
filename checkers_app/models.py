from django.db import models

from django.contrib.auth.models import User

from jsonfield import JSONField

# Create your models here.

# class User(models.Model):
#     title       = models.TextField(max_length=120)
#     description = models.TextField(blank=True,null=True)
#     price       = models.DecimalField(decimal_places=2, max_digits=10000)
#     summary     = models.TextField(default='add something!')
#     # featured    = models.BooleanField()


class UserMoves(models.Model):
    last_move = models.CharField(max_length=50, default='computer')
    moves = JSONField(default={'hernan':["1", "1", "0", "2", "2", "1", "0", "2", "0"]})

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  
    # def __str__(self):
    #     return self.moves