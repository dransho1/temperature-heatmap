from django.contrib import admin

from .models import Sensor, Feed

admin.site.register(Sensor)
admin.site.register(Feed)