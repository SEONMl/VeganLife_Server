from django.db import models

# Create your models here.


class Member(models.Model):
    class Meta:
        db_table='member'
    id=models.IntegerField(primary_key=True)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    vege_type = models.CharField(max_length=100)


