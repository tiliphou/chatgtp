from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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
        return HttpResponse("content")


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
        return HttpResponse("content")

@login_required
def removeroom(request, slug):
    if request.method == 'POST':
        try:
            room = Room.objects.get(slug=slug)
        except Room.DoesNotExist:
            return HttpResponse("The room does not exist.")
        if not request.user.is_staff:
            return HttpResponse("You are not authorized to remove this room.")
        room.delete()
        return HttpResponse('nothing')


@login_required
def updatemessage(request,slug):
    if request.method == 'GET':
        messages = list(Message.objects.all().values())
        return JsonResponse({'messages': messages})

@login_required
def updateroom(request,slug):
    if request.method == 'GET':
        rooms = list(Room.objects.all().values())
        return JsonResponse({'rooms':rooms})




