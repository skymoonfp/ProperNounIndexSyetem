# Register your models here.

from django.contrib import admin

from Main import models

admin.site.register(models.UserInfo)
admin.site.register(models.UserClass)
admin.site.register(models.Books)
admin.site.register(models.ProperNounIndex)
admin.site.register(models.NounProperty)
