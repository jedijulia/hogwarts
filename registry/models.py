from __future__ import unicode_literals

from django.db import models


class House(models.Model):
    name = models.CharField(max_length=150)
    head = models.CharField(max_length=150)
    points = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.DateField()
    year = models.PositiveIntegerField()
    house = models.ForeignKey(House, related_name='students')
    wand = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name
