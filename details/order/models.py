from django.db import models

from tkinter import CASCADE
from django.db import models
from customer.models import customer
from product.models import product

class order1(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    unit_price=models.IntegerField()
    total_price=models.IntegerField()
    

    class Meta:
        db_table="order_table"

        



