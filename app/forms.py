from django import forms
from .models import GENDER_CHOICES

GENDER_CHOICES = GENDER_CHOICES + [('', '---------')]

class ProfileSearchForm(forms.Form):
    gender = forms.ChoiceField(label='Sex', choices=GENDER_CHOICES, required=False)
    yearly_income = forms.IntegerField(label='saraly (above)', required=False)
    height = forms.FloatField(label='Height (above)', required=False)
    weight = forms.FloatField(label='Weight (below)', required=False)


ProfileSearchFormSet = forms.formset_factory(ProfileSearchForm, extra=3)