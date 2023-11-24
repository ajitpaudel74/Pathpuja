from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('puja/<str:pk>',views.puja,name="puja"),
    path('puja-list/',views.puja_list,name="puja_list"),
    path('login/',views.login,name="login"),
    path('register/',views.register, name="register")

]