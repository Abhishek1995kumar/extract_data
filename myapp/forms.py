from django import forms
from .models import *
class extract_imageForm(forms.ModelForm):
   class Meta:
      model = extract_image
      fields = ['due_date', 'account_no','bill_amount']