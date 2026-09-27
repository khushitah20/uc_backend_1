from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["event_name","date","venue","club","status"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"}),}