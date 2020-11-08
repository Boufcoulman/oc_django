from django.urls import re_path

from . import views  # import views so we can use them in urls.


urlpatterns = [
    re_path(r'^$', views.listing),
]
