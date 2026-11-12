from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='team_list'),
    path('<str:team_name>/', views.team_detail, name='team_detail'),
]