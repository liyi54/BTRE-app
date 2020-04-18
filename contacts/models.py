from django.db import models
from listings.models import Listing
from django.utils import timezone

class Contacts(models.Model):
    listing = models.CharField(max_length=100)
    listing_id = models.IntegerField(blank=True, default=0)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=1000, blank=True)
    inquiry_date = models.DateTimeField(default=timezone.now())
    user_id = models.IntegerField(blank=True)   # Since not all users must be logged in to make an inquiry, we make it optional

    def __str__(self):
        return self.name
