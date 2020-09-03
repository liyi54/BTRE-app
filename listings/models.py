from django.db import models
from django.utils import timezone
from realtors.models import Realtor
from cloudinary.models import CloudinaryField

class Listing(models.Model):
    # This allows us setup our schema easily rather than use raw SQL statements
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathroom = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    list_date = models.DateTimeField(default=timezone.now(), blank=True)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=4, decimal_places=1)
    photo_main = CloudinaryField('image')
    photo_1 = CloudinaryField('image')
    photo_2 = CloudinaryField('image')
    photo_3 = CloudinaryField('image')
    photo_4 = CloudinaryField('image')
    photo_5 = CloudinaryField('image')
    photo_6 = CloudinaryField('image')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title