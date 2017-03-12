from django.db import models

# Create your models here.
from .gmaps import LocationDetails


class DonerDetails(models.Model):

    choices = ((True, 'Yes'), (False, 'No'))

    name = models.TextField(max_length=20)
    class_dept = models.TextField(max_length=50)
    college = models.TextField(max_length=150)
    address = models.TextField(max_length=300)
    blood_group = models.TextField(max_length=10)
    recently_donated = models.BooleanField(choices=choices)
    phone_number = models.IntegerField()
    location = models.TextField(max_length=100)
    district = models.TextField(max_length=100, default='Trivandrum')

    def get_cord(self):
        return LocationDetails().get_geocode(self.location)

    def change_donation_status(self, status):
        self.recently_donated = status

    def __str__(self):
        return self.name + " " + self.blood_group

    def save(self, *args, **kwargs):
        if not self.coordinates3:
            self.coordinates3 = self.get_cord()
            super(DonerDetails, self).save(*args, **kwargs)

