from django.forms import ModelForm
from django import forms
from .models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = []
        widgets = {
            'user_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'details' : forms.Textarea(attrs={'class':'form-control'}),
            
        } 
