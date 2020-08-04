from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='blog-home'),
    #empty path pr humne views.py me home fucntion call kiya and name dedio blog-home
]
