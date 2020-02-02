from django.urls import path
from .views import  index,delete,add_img

urlpatterns = [
    path('', index),
    path('add_img', add_img),
    path('delete', delete),
]