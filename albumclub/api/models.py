from django.db import models

# Commented out imports kept for future changes to the code
# from django.conf import settings
# from django.utils import timezone

class Album(models.Model): #this is how Django knows this is a model class
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    artwork = models.URLField(max_length=200)
    # Each attribute of the model represents a database field


    def __str__(self): #def __str__(self) is how you create a method on the Album objects
        return self.title + ':'+ ' '+ self.artist #Returns a string using Album attributes to Admin Page 

    
    # Commented out code kept in for future changes to the code
    # def publish(self):
    #     self.published_date = timezone.now()