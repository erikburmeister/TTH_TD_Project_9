from django import forms

from .models import Menu, Item, Ingredient

class DateInput(forms.DateInput):
    input_type = 'date'

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ('created_date',)
        widgets = {'expiration_date': DateInput()}

    def clean(self):
        season = self.cleaned_data['season']

        if not season:
            raise forms.ValidationError(
                "Add a name for the Season.")