from . import views
from django.urls import include, path


urlpatterns = [
    path('',views.get_url,name='get-URL'),
]
