from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField('image')
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
