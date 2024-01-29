from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register_user, name = 'Register'),
    path('logout/', views.logout_user, name = 'logout'),
]