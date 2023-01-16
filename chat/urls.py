from django.urls import path

from . import views

urlpatterns = [ 
    path('',views.rooms,name="rooms"),
    path('createroom/', views.createroom,name="createroom"),
    path('<slug:slug>/', views.room, name='room'),
    path('<slug:slug>/sendmessage/',views.sendmessage,name='sendMessage'),
]