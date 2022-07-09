from django.db import models


# Create your models here.


class Nutrients(models.Model):
    class Meta:
        db_table = 'nutrients'

    calcium = models.FloatField()
    vitamin = models.FloatField()
    iron = models.FloatField()


class Diet(models.Model):
    class Meta:
        db_table = 'diet'

    intake_time = models.DateTimeField()
    name = models.TextField()
    calorie = models.FloatField()
    carbohydrate = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    calcium = models.FloatField()
    vitamin = models.FloatField()
    iron = models.FloatField()
