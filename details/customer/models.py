from django.db import models

from django.db import models


class customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    pincode=models.IntegerField()

