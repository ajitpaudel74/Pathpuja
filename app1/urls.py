from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('puja/<str:pk>',views.puja,name="puja"),
    path('puja-list/',views.puja_list,name="puja_list"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.register, name="register")

]