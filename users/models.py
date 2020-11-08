from django.db import models

# Create your models here.
from django.urls import reverse

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('user_edit', kwargs={'pk': self.pk})

    