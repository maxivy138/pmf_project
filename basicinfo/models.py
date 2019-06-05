from django.db import models
from datetime import datetime

class Info(models.Model):
    financetype = models.CharField(max_length=100)
    credittype = models.CharField(max_length=100)
    propvalue = models.CharField(max_length=100)
    firstmortgagebalance = models.CharField(max_length=100)
    firstmortgagerate = models.CharField(max_length=100)
    secondmortgagebalance = models.CharField(max_length=100)
    secondmortgagerate = models.CharField(max_length=100)
    borrowamount = models.CharField(max_length=100)
    incometype = models.CharField(max_length=100)
    incomerange = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name