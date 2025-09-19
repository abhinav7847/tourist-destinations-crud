
from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=200)
    weather = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    google_map_link = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.place_name


class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="destination_images/")

    def __str__(self):
        return f"Image for {self.destination.place_name}"