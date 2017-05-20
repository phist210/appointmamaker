from django import forms
from .models import Appointment
from django.forms.extras.widgets import SelectDateWidget


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget)
    time = forms.TimeField(widget=forms.TextInput, help_text='HH:MM:SS')
    description = forms.CharField(widget=forms.TextInput, help_text='50 chars')

    class Meta:
        model = Appointment
        fields = "__all__"
