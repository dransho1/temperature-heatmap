from django.db import models

from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Sensor(models.Model):
    sensor_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sensor_name

@python_2_unicode_compatible
class Feed(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    feed_name = models.CharField(max_length=200)
    temperature = models.FloatField()

    def __str__(self):
        return self.feed_name

    def above_room_temp(self):
        return self.temperature >= 70.0