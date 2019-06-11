# Register your models here.

from django.contrib import admin

from Main import models


class UserInfoAdmin(admin.ModelAdmin):
    list_display = (
    "id", "username", "password", "birthday", "e_mail", "mobile", "identify_code", "create_time", "user_class")
    search_fields = (
    "id", "username", "password", "birthday", "e_mail", "mobile", "identify_code", "create_time", "user_class")
    list_filter = ("birthday", "e_mail", "mobile", "create_time", "user_class")


class UserClassAdmin(admin.ModelAdmin):
    list_display = ("id", "user_class_name")
    search_fields = ("id", "user_class_name")
    list_filter = ("user_class_name",)


class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "book_name", "author", "translator", "ISBN", "edition", "publication_date", "create_time")
    search_fields = ("id", "book_name", "author", "translator", "ISBN", "edition", "publication_date", "create_time")
    list_filter = ("book_name", "author", "translator", "edition", "publication_date", "create_time")


class ProperNounIndexAdmin(admin.ModelAdmin):
    list_display = (
    "id", "book_name", "ISBN", "Noun", "page", "noun_property", "classes", "relation", "comment", "context",
    "create_time")
    search_fields = (
    "id", "book_name", "ISBN", "Noun", "page", "noun_property", "classes", "relation", "comment", "context",
    "create_time")
    list_filter = ("book_name", "Noun", "page", "noun_property", "classes", "relation", "comment", "create_time")


class NounPropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "noun_property_name")
    search_fields = ("id", "noun_property_name")
    list_filter = ("noun_property_name",)


admin.site.register(models.UserInfo, UserInfoAdmin)
admin.site.register(models.UserClass, UserClassAdmin)
admin.site.register(models.Books, BooksAdmin)
admin.site.register(models.ProperNounIndex, ProperNounIndexAdmin)
admin.site.register(models.NounProperty, NounPropertyAdmin)
