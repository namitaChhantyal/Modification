from django.db import models

class Page(models.Model):
    Houseno=models.IntegerField()
    Ownersname=models.CharField(max_length=255)

# class Payment(models.Model):
#     payment_amount=models.IntegerField()