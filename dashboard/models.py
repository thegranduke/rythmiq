from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)

class Audio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audios/')
    upload_date = models.DateTimeField(auto_now_add=True)
