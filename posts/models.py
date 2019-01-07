from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Activity(models.Model):
    activity_type = models.CharField(max_length=10)
    post_id = models.CharField(max_length=200)
    post_title = models.TextField(help_text='Contents of the post')
    user_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=100)
    comment_id = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(
            blank=True, 
            null=True,
            help_text='Comment for this post'
            )

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'post_id':self.post_id})

    def __str__(self):
        return self.activity_type + '_' + self.post_id


