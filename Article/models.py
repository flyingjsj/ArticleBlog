from django.db import models


# Create your models here.

class type(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        db_table = "type"


class author(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField(max_length=32)
    type = models.ManyToManyField(to=type)

    class Meta:
        db_table = "author"


class Article(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(to=author, to_field="id", on_delete=models.CASCADE)
    click = models.IntegerField(default=0)

    class Meta:
        db_table = "Article"


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"
