from django.db import models
from user.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    image = models.FileField(upload_to='static/media/')
    tag = models.CharField(max_length=500, default='#tech')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()
    email = models.EmailField(null=False, blank=False)
    name = models.CharField(blank=False, default='', max_length=35)

    def __str__(self):
        return self.email

