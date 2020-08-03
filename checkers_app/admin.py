from django.contrib import admin

# Register your models here.

from .models import UserMoves, Contact

# admin.site.register(User)
admin.site.register(UserMoves)
admin.site.register(Contact)
