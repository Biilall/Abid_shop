from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    
    first_name = models.CharField(max_length=300)
    second_name = models.CharField(max_length=300)
    old_password = models.CharField(max_length=300)
    new_password = models.CharField(max_length=300)
    mobile = models.CharField(max_length=300)
    username = models.CharField(max_length=60)
   
    def __str__(self):
        return self.username

class Expense(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    comment = models.CharField(max_length=300)
    cash = models.CharField(max_length=300)
   
    def __str__(self):
        return self.comment

class Exchange(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    item = models.CharField(max_length=300)
    weight = models.CharField(max_length=300)
    whereTo = models.CharField(max_length=300)
   
    def __str__(self):
        return self.item

class Sell(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    stock = models.CharField(max_length=300)
    item = models.CharField(max_length=300)
    weight = models.CharField(max_length=300)
    cash = models.CharField(max_length=300)
    profit = models.CharField(max_length=300)
    bm = models.CharField(max_length=300)
   
    def __str__(self):
        return self.item

class Pruchase(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    shop_cash = models.CharField(max_length=300)
    item = models.CharField(max_length=300)
    weight = models.CharField(max_length=300)
    cash = models.CharField(max_length=300)
    profit = models.CharField(max_length=300)
    bm = models.CharField(max_length=300)
    scrape = models.CharField(max_length=300)
   
    def __str__(self):
        return self.item
