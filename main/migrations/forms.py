from django import forms
from.models import snippest

class rainfallforms(forms.forms):
class DateInput(forms.DateInput):
classExampleForm(forms.forms):
my-date-field= forms.DateField()

class snippestform(forms.modelsform):

  class meta:
    model=snippest
    fields='','body'