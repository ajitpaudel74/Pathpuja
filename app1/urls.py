from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('puja/<str:pk>',views.puja,name="puja"),
    path('puja-list/',views.puja_list,name="puja_list"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.register, name="register"),
    path('book-pandit/<str:pk>/<str:pdt>',views.BookPandit,name="book_pandit"),
    path('pandit_profile/<str:pk>',views.panditProfile,name="pandit_profile"),
    path('profile',views.userProfile,name="user_profile"),
    path('cancel_booking/<str:pk>',views.cancelBooking,name="cancel_booking")

]