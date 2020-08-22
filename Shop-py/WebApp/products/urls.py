from django.urls import path
from . import views

urlpatterns = [
    path("", views.prod_index, name="prod_index"),
]
