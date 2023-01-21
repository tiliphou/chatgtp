from django.urls import path

from . import views

urlpatterns = [ 
    path('',views.rooms,name="rooms"),
    path('createroom/', views.createroom,name="createroom"),
    path('updateroom/',views.updateroom,name='updateroom'),
    path('<slug:slug>/', views.room, name='room'),
    path('<slug:slug>/sendmessage/',views.sendmessage,name='sendMessage'),
    path('<slug:slug>/updatemessage/',views.updatemessage,name='updatemessage'),
    path('removeroom/<slug:slug>/', views.removeroom,name="removeroom"),
]