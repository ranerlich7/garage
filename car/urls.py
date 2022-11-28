from django.urls import path
from . import views

app_name="car"
urlpatterns = [
    path('t', views.treatment, name="t"),
    path('list', views.treatments, name="tlist")
]
