from django.forms import ModelForm
from .models import Roles

class RolesForm(ModelForm):
    class Meta:
        model = Roles
        fields = ['is_admin']
        labels = {
            'is_admin': ''
        }