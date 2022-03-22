from time import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Memo(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f' This memo is about {self.title}'
    
    def get_absolute_url(self):
        return reverse('memos_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ('-date', 'title')