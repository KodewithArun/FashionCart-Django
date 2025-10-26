from django.urls import path
from . import views

urlpatterns = [
    # add custom urls here for project: by Arun
    path("", views.cart, name="cart"),
    
]
