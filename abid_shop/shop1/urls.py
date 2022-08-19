from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',
         views.index ),
    # path('login/',
        #  views.get_account, name='login' )
    # path('code/',
    #      views.get_code, name='code' )
]