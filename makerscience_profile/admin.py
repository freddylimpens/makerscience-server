from django.contrib import admin
from .models import MakerScienceProfile
from django.contrib.admin.options import ModelAdmin
from accounts.models import Profile, ObjectProfileLink

# try:
#     admin.site.unregister(Profile)
# except:
#     pass

admin.site.register(MakerScienceProfile, ModelAdmin)
admin.site.register(ObjectProfileLink, ModelAdmin)
