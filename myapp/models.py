# Create your models here.
from __future__ import unicode_literals

from django.db import models


class fields(models.Model):

     Fields=models.CharField(max_length=100)

     def __str__(self):
         return(self.Fields)


class software(models.Model):

    fi_elds=models.ForeignKey(fields,on_delete=models.CASCADE, null=True)
    Description=models.CharField(max_length=1000)
    inclusion=models.CharField(max_length=200)
    price=models.CharField(max_length=20)
    title=models.CharField(max_length=100)


    def __str__(self):
         return(self.title)
