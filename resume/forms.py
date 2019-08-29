from django import forms

class JsonForm(forms.Form):
  json = forms.CharField(widget=forms.Textarea, label='JSON')
