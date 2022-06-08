from django.urls import path
from . import views

# Here . means current folder

# /products ->
urlpatterns = [
    path('',views.index),
    path('new',views.new)
]


#when we want to add new module to our app first make function in views.py and then add it to products/urls.py in urlpatterns variable