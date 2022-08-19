from django.contrib import admin

# Register your models here.
from .models import User, Exchange, Expense, Sell, Pruchase

admin.site.register(User)
admin.site.register(Exchange)
admin.site.register(Expense)
admin.site.register(Sell)
admin.site.register(Pruchase)
