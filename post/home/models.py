from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/post_pictures',default='uploads/post_pictures/default.png', blank=True)
    likes = models.IntegerField(default=0)
    authorr = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # image = models.ImageField(null=True)
    image = models.ImageField(upload_to='uploads/profile_pictures',default='uploads/profile_pictures/default.png', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'



   