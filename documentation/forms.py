
from django import forms

from .models import Cotation


class CotationForm(forms.ModelForm):

    class Meta:
        model = Cotation
        fields = ('proj_name', 'subject_name', 'doc_name_pattern','doc_name', 'cod_doc_type','page_type','format_doc','qt_page', 'qt_hh','cost_doc')
