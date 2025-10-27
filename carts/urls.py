from django.urls import path
from . import views

urlpatterns = [
    # add custom urls here for project: by Arun
    path("", views.cart, name="cart"),
    # add to cart
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    # remove from cart
    path("remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    # delete from cart entirely
    path("delete/<int:product_id>/", views.delete_from_cart, name="delete_from_cart"),
]
