from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.prod_index, name="prod_index"),
    path("index",views.show_list,name="GET_POST_REQUEST"),
]+ static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
