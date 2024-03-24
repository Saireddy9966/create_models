from django.db import models

# Create your models here.

class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eadd=models.CharField(max_length=64)

    def __str__(self):
        return self.ename
