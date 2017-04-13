"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Present(models.Model):
    name = models.CharField(max_length=200)
    cost = models.FloatField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    url = models.URLField(blank=True)
    buyed = models.BooleanField(default=False)
    date_buyed = models.DateTimeField('Date Buyed', blank=True, null=True)
    date_inserted = models.DateTimeField('Date Inserted')
    friendPresent = models.ManyToManyField(User, through='FriendPresent')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('present-detail', kwargs={'pk': self.pk})

class FriendPresent(models.Model):
    present = models.ForeignKey(Present, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    date_interest = models.DateTimeField('Date Interest')
    confirmed = models.BooleanField(default=False)

