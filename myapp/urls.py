from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('home/', views.homePage, name="home"),
]
