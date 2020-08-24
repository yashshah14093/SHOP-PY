from django.urls import path
from . import views

urlpatterns = [
    path("", views.prod_index, name="prod_index"),
    path("index",views.show_list,name="GET_POST_REQUEST"),
]
