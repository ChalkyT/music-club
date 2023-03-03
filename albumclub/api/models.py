from django.conf import settings
from django.db import models
from django.utils import timezone

class Album(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    artwork = models.URLField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title + ':'+ ' '+ self.artist
