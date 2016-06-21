from django.db import models
from taggit.managers import TaggableManager


class Person(models.Model):
    name = models.CharField('姓名', max_length=20)

    def __str__(self):
        return self.name

class MovieRole(models.Model):
    name = models.CharField('角色', max_length=20)

    def __str__(self):
        return self.name

class Gene(models.Model):
    name = models.CharField('类型', max_length=20)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField('片名', max_length=100)
    original_name = models.CharField('原名', max_length=100, blank=True, null=True)
    intro = models.TextField('简介', blank=True, null=True)
    storage_folder = models.FilePathField('目录', blank=True, null=True)
    year = models.IntegerField('年份', blank=True, null=True)
    imdb = models.CharField(max_length=15, blank=True, null=True)
    douban = models.CharField(max_length=15, blank=True, null=True)
    tags = TaggableManager(blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return "{}({})".format(self.name, self.year)

class Aka(models.Model):
    movie = models.ForeignKey(Movie)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} Aka {}".format(self.movie.name, self.name)

class MoviePerson(models.Model):
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    role = models.ForeignKey(MovieRole)

    def __str__(self):
        return "{} as {} for {}".format(self.person.name, self.role.name, self.movie.name)

class MovieGene(models.Model):
    movie = models.ForeignKey(Movie)
    gene = models.ForeignKey(Gene)

    def __str__(self):
        return "{} is {}".format(self.movie.name, self.gene.name)
