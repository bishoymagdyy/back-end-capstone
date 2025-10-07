from django.contrib import admin
from . import models
from rest_framework.authtoken.models import Token

# Register your models here.
admin.site.register(models.Booking)
admin.site.register(models.MenuItem)
admin.site.register(Token)