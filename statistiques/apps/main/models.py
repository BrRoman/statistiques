""" apps/main/models.py """

from django.db import models


class Moine(models.Model):
    """ Moine model. """
    name = models.CharField(
        max_length=25,
        db_column='nom',
    )
    birth = models.DateField(
        db_column='naissance',
    )
    rank = models.SmallIntegerField(
        db_column='rang',
    )
    entry = models.DateField(
        db_column='entree',
    )
    habit = models.DateField(
        db_column='prise_habit',
    )
    temporary_profession = models.DateField(
        db_column='prof_temp',
    )
    perpetual_profession = models.DateField(
        db_column='prof_perpet',
    )
    ordination = models.DateField(
        db_column='ordination',
    )

    class Meta:
        managed = False
        db_table = 'Moines'

    def __str__(self):
        return self.name
