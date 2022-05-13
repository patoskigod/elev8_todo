#urls file for app

from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('signup',views.sign,name='signup'),
    path('edit',views.edit,name='edit'),
    path('profile',views.profile,name='profile'),
    path('login',views.log,name='login'),
    path('users',views.users,name='users'),
    
    
]