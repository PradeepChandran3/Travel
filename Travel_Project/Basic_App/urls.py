from . import views
from django.urls import path

urlpatterns = [
    # (Function 1,2,3,4)
    path('basic', views.base, name='base'),

    # (Funtion 4)
    path('add/', views.addition, name='addition'),
]