from time import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
###from datetime import datetime###

Roles = (
    ('U', 'General User'),
    ('A', 'Admin User'),
)

class Org(models.Model):
    org_id = models.IntegerField(unique=True, auto_created=True)
    org_name = models.CharField(max_length=256)

    def __str__(self):
        return self.org_name

class Tag(models.Model):
    tag_id = models.IntegerField(unique=True, auto_created=True)
    tag_desc = models.CharField(max_length=25)

    def __str__(self):
        return self.tag_desc

class Memo(models.Model):
    
    memo_title = models.CharField(max_length=100)
    memo_create_date = models.DateField(auto_now=True)
    memo_text = models.CharField(max_length=5000, default='missing')
    tag = models.ManyToManyField(Tag) 
    org= models.ManyToManyField(Org)


    def __str__(self):
        return f'Memo: {self.memo_title} from {self.memo_create_date}'
    
    def get_absolute_url(self):
        return reverse('memos_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ('-memo_create_date', 'memo_title')


class Roles(models.Model):
    role_id = models.IntegerField(unique=True, auto_created=True)
    role_desc = models.CharField(max_length=25, choices=Roles, default=Roles[0][0])

    def __str__(self):
        return f'user type: {self.get_roles_display()}'