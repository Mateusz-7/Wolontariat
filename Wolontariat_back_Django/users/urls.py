from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='Login'),
    path('logout', views.logout_view, name='Logout'),
]
