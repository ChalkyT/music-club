from django.contrib import admin
from .models import Album # retrieving our album model from .models ('.' means same directory)

#This is where you register the tables you want to show up in the Django Admin page
#You only need to add this file if you want to make use of the Admin pages to access/update album info
admin.site.register(Album)

# Refresh the server after registering a model
# Now the Admin pages with have Groups, Users and Albums tables
# You can then add new Albums, Users and Groups via the Admin page
