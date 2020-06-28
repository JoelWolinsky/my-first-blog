from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    first_para = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    cover = models.ImageField(upload_to='images/')

    


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title