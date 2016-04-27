__author__ = 'anuraagbasu'

from django.db import models
from datetime import datetime

class Track (models.Model):
    title = models.CharField(max_length=200)
    createDate = models.DateTimeField(default=datetime.now())
    rating = models.IntegerField(default=0)
    genres = models.ManyToManyField('Genre')
    def getRatingIterable(self):
        return range(0, self.rating)
    def getRemainingRatingiterable(self):
        return range(0, 5-self.rating)
    def getGenresAsString(self):
        genresAsString = ""
        for genre in self.genres.all():
            genresAsString = genresAsString + " | "
            genresAsString = genresAsString + genre.name

        print(genresAsString)
        print(genresAsString!="")
        if genresAsString!="":
            value = "[" + genresAsString[3:] + "]"
            return value
        else:
            return genresAsString


class Genre (models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000, blank=True)
