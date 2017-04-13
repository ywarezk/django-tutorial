from django.forms import forms, fields, models
from hello.models import Greeting

class GreetingForm(models.ModelForm):
    class Meta:
        model = Greeting
        exclude = ('slug', )