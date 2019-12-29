from django.contrib import admin
from .models import RocketLaunchData,LaunchSiteData,Facts,Learn,PreviousLaunchData

# Register your models here.
admin.site.register(RocketLaunchData)
admin.site.register(LaunchSiteData)
admin.site.register(Facts)
admin.site.register(Learn)
admin.site.register(PreviousLaunchData)
