from django import forms
from .models import Lap_Model
class Lap_Form(forms.ModelForm):
    class Meta:
        model = Lap_Model
        fields = "__all__"