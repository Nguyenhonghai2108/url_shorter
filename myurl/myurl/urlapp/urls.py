from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list_url, name='list'),
    path('detail/<alias>/', views.detail, name='detail')
]