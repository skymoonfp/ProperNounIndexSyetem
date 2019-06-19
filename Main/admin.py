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


class ProperNounAdmin(admin.ModelAdmin):
    list_display = ("id", "Noun", "classes", "properties", "relation", "comment", "create_time")
    search_fields = ("id", "Noun", "book", "category", "classes", "properties", "relation", "comment", "create_time")
    list_filter = ("Noun", "book", "category", "classes", "properties", "create_time")


class BookNounIndexAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "Noun", "page", "context", "create_time")
    search_fields = ("id", "book", "Noun", "page", "context", "create_time")
    list_filter = ("book", "Noun", "create_time")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")
    search_fields = ("id", "category")
    list_filter = ("category",)


admin.site.register(models.UserInfo, UserInfoAdmin)
admin.site.register(models.UserClass, UserClassAdmin)
admin.site.register(models.Books, BooksAdmin)
admin.site.register(models.ProperNoun, ProperNounAdmin)
admin.site.register(models.BookNounIndex, BookNounIndexAdmin)
admin.site.register(models.Category, CategoryAdmin)
