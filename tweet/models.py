from django.db import models
from django.contrib.auth.models import User # Importing User model
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text = models.TextField(max_length=280)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField

def __str__(self):
    return f'{self.user.username} - {self.text[:10]}'  # Display first 10 characters of the tweet text
