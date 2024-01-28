from . import views
from django.urls import include, path


urlpatterns = [
    path('shorten/',views.shortenURL,name='shorten-URL'),
]
