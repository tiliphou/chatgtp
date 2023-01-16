from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify
from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'chat/rooms.html', {'rooms': rooms})
    


@login_required
def createroom(request):
    if request.method == 'POST':
        room_name = request.POST["name"]
        room = Room(name=room_name,slug=room_name)
        room.save()
        return HttpResponse('nothing')


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room.html', {'room': room, 'messages': messages})


@login_required
def sendmessage(request,slug):
    if request.method == 'POST':
        content = request.POST['content']
        room_pass=request.POST['room']
        room = Room.objects.get(slug=room_pass)
        user_pass = request.POST['name']
        user = User.objects.get(username=user_pass)
        new_Message = Message(content=content,user=user,room=room)
        new_Message.save()
        return HttpResponse(content)
