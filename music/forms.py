__author__ = 'anuraagbasu'

from django.db import models

class TrackForm (ModelForm):
    class Meta:
        model = Track

class GenreForm (ModelForm):
    class Meta:
        model = Genre