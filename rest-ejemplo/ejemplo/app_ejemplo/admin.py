from django.contrib import admin

from app_ejemplo import models

# Register your models here.
admin.site.register(models.Recipe)
admin.site.register(models.Tag)