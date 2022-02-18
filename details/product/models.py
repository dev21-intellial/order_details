from django.db import models

from django.db import models



class product(models.Model):
    name=models.CharField(max_length=100)
    unit_price=models.IntegerField()

    class Meta:
        db_table="product_table"

        
