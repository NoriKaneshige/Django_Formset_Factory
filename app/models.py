from django.db import models


GENDER_CHOICES = [
    ('1', 'female'),
    ('2', 'male'),
]


class Profile(models.Model):
    name = models.CharField('name', max_length=100)
    gender = models.CharField('sex', max_length=1, choices=GENDER_CHOICES)
    yearly_income = models.IntegerField('salary(K)')
    height = models.FloatField('height')
    weight = models.FloatField('weight')