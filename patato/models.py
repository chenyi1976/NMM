from django.db import models
from taggit.managers import TaggableManager


class Person(models.Model):
    name = models.CharField('姓名', max_length=20)


class MovieRole(models.Model):
    name = models.CharField('角色', max_length=20)


class Movie(models.Model):
    name = models.CharField('片名', max_length=100)
    intro = models.TextField('简洁', blank=True, null=True)
    storage_folder = models.FilePathField('目录', null=True)
    year = models.IntegerField('年份', null=True)
    imdb = models.CharField(max_length=15, null=True)
    douban = models.CharField(max_length=15, null=True)
    tags = TaggableManager()


class Aka(models.Model):
    movie = models.ForeignKey(Movie)
    name = models.CharField(max_length=100)


class MoviePerson(models.Model):
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    role = models.ForeignKey(MovieRole)
