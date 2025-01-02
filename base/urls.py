#from django.contrib import admin
from django.urls import path

#from django.http import HttpResponse


from . import views

from django.shortcuts import render

from django.urls import path

#from django.contrib import admin
#from django.urls import path,include
# Create your views here.


urlpatterns=[
    
    path('login/',views.loginPage,name="login"),
    #path('',views.UserVerify,name="user"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),

    path('',views.home,name="home"),
    #path('',views.purchase,name="purchase"), 
    path('room/<str:pk>/',views.room,name="room"),
    path('profile/<str:pk>',views.userProfile,name="user-profile"),
    #Passing dynamic value with data type specified.
    #pk- primary key.

    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>',views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>',views.deleteMessage,name="delete-message"),
    path('update-user/',views.updateUser,name="update-user"),
    #path('delete-topic/<str:pk>',views.deleteTopic,name="delete-topic")
    path('topics/',views.topicsPage,name="topics"),
    path('activity/',views.activityPage,name="activity")
]

