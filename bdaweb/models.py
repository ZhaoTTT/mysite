from django.db import models

from django.contrib import admin

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=15)

    def __str__(self):
        return self.userid


# class Item(models.Model):
#     todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()

#     def __str__(self):
#         return self.text

class itemCFrecommendation(models.Model):
    userid = models.CharField(max_length=15)
    asin = models.CharField(max_length=15)
    rating = models.IntegerField()
    imageURL = models.CharField(max_length=200)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class CBrecommendation(models.Model):
    asin = models.CharField(max_length=15)
    asin_rec = models.CharField(max_length=15)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    imageURL = models.CharField(max_length=200)

    def __str__(self):
        return self.title