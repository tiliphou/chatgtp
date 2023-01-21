from django.db import models
from django.contrib.auth.models import User



class Room(models.Model):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(default="")
    def __str__(self):
        return self.content


