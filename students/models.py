from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    gpa = models.FloatField()
    course = models.IntegerField()