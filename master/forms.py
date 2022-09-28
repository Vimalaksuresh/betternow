import email
from email import message
from unicodedata import name
from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField()
    subject=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)




