"""
Definition of forms.
"""

from django.forms import ModelForm
from .models import Present

class PresentForm (ModelForm) :
    class Meta:
        model = Present
        fields = ['name', 'cost', 'url']


