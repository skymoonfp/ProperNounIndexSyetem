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
    user_class = models.ForeignKey("UserClass", default=1, null=True, on_delete=models.SET_NULL)


class UserClass(models.Model):
    user_class = models.CharField(max_length=50, unique=True)


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
    ISBN = models.CharField(max_length=20, null=True)

    Noun = models.CharField(max_length=30)

    page = models.CharField(max_length=20)

    property_CHOICE = (
        (u'P', u'Person'),
        (u'L', u'Location'),
        (u'O', u'Other'),
    )
    noun_property = models.CharField(max_length=2, choices=property_CHOICE)

    classes = models.CharField(max_length=30, null=True)
    relation = models.CharField(max_length=60, null=True)
    comment = models.CharField(max_length=60, null=True)
    context = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
