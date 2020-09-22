from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]
