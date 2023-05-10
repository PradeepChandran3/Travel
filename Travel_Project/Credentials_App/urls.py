from.import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='reg'),
    path('login', views.login, name='log'),
    path('logout', views.logout, name='lout')

]
