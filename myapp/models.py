import uuid

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"


class Booking(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    booking_date = models.DateField(null=True, blank=True)
    booking_time = models.CharField(max_length=20)
    guests = models.CharField(max_length=10)
    added_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Comment(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name