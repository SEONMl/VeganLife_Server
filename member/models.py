from django.db import models


# Create your models here.


class Member(models.Model):
    class Meta:
        db_table = 'member'
    email = models.EmailField(unique=True)
    password = models.TextField()
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True)
    height = models.FloatField()
    weight = models.FloatField()
    vege_type = models.CharField(max_length=100)

    def __str__(self):
        return self.email