# Create your models here.


from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    e_mail = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    identify_code = models.CharField(max_length=20, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    user_class = models.ForeignKey("UserClass", null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "用户信息表"


class UserClass(models.Model):
    user_class_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user_class_name

    class Meta:
        verbose_name_plural = "用户类型表"


class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True, blank=True)
    translator = models.CharField(max_length=50, null=True, blank=True)
    ISBN = models.CharField(max_length=20, null=True, blank=True)
    edition = models.CharField(max_length=10, null=True, blank=True)
    publication_date = models.CharField(max_length=6, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name_plural = "书籍表"


class ProperNoun(models.Model):
    Noun = models.CharField(max_length=30)
    book = models.ManyToManyField('Books', through='BookNounIndex', max_length=30)
    category = models.ManyToManyField('Category', null=True, blank=True)
    classes = models.CharField(max_length=30, null=True, blank=True)
    properties = models.CharField(max_length=60, null=True, blank=True)
    relation = models.CharField(max_length=60, null=True, blank=True)
    comment = models.CharField(max_length=60, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.Noun

    class Meta:
        verbose_name_plural = "专名表"


class BookNounIndex(models.Model):
    book = models.ForeignKey('Books', on_delete=models.CASCADE)
    Noun = models.ForeignKey('ProperNoun', on_delete=models.CASCADE)
    page = models.CharField(max_length=20)
    context = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = "专名索引表"


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "专名范畴表"
