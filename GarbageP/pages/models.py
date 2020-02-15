from django.db import models

class Page(models.Model):
    Houseno=models.IntegerField(primary_key=True)
    Ownersname=models.CharField(max_length=255)
    # password=models.CharField(max_length=255)
    def _str_(self):
        return self.page_text

class Payment(models.Model):
    Houseno=models.IntegerField()
    Due_amount=models.IntegerField()
    Month=models.CharField(max_length=255)
    Fine=models.IntegerField()