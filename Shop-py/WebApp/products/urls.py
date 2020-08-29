from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import HomePageView


urlpatterns = [
    #path("", views.prod_index, name="prod_index"),
    path("index",views.show_list,name="GET_POST_REQUEST"),
    path('', HomePageView.as_view(), name='index'),
]
