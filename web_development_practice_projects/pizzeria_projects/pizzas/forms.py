"""Define Form for adding pizza and topping"""

from django import forms
from .models import Topping, Pizza

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        labels = {'text': ''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = '__all__'
        exclude = ['pizza']
        labels = {'text': ''}