from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    path('sign_up',views.SignUp.as_view(),name="signup"),
    path('login',views.LogIn.as_view(),name="login"),
    path('logout',views.Logout.as_view(),name="logout")
]