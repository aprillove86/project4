from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Memo(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f' This memo is about {self.title}'
    
    def get_absolute_url(self):
        return reverse('memos_detail', kwargs={'pk': self.id})


# Create your models here.
