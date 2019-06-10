# Create your models here.


from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    e_mail = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=20, null=True)
    identify_code = models.CharField(max_length=20, null=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    user_class = models.ForeignKey("UserClass", null=True, on_delete=models.SET_NULL)


class UserClass(models.Model):
    user_class_name = models.CharField(max_length=50, unique=True)


class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    translator = models.CharField(max_length=50, null=True)
    ISBN = models.CharField(max_length=20, null=True)
    edition = models.CharField(max_length=10, null=True)
    publication_date = models.CharField(max_length=6, null=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)


class ProperNounIndex(models.Model):
    book_name = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    Noun = models.CharField(max_length=30)
    page = models.CharField(max_length=20)
    noun_property = models.ForeignKey('NounProperty', to_field="id", null=True, on_delete=models.SET_NULL)
    classes = models.CharField(max_length=30, null=True)
    relation = models.CharField(max_length=60, null=True)
    comment = models.CharField(max_length=60, null=True)
    context = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)


class NounProperty(models.Model):
    noun_property_name = models.CharField(max_length=20)

    def __str__(self):
        return self.noun_property_name
