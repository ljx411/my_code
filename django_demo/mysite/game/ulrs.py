from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.get_5566, name='5566')
]
