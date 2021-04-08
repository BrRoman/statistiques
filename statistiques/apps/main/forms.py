""" apps/main/forms.py """

from django import forms

from tempus_dominus.widgets import DatePicker

from .models import Monk


class MonkForm(forms.ModelForm):
    """ Form for Monk. """
    name = forms.CharField(
        max_length=255,
        label='Nom :',
        label_suffix='',
    )
    birth = forms.DateField(
        required=False,
        label='Date de naissance :',
        label_suffix='',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
            }
        ),
    )
    entry = forms.DateField(
        required=False,
        label='Entrée :',
        label_suffix='',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
            },
        ),
    )
    habit = forms.DateField(
        required=False,
        label='Prise d\'habit :',
        label_suffix='',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
            }
        ),
    )
    temporary_profession = forms.DateField(
        required=False,
        label='Profession temporaire :',
        label_suffix='',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
            }
        ),
    )
    perpetual_profession = forms.DateField(
        required=False,
        label='Profession perpétuelle :',
        label_suffix='',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
            }
        ),
    )
    ordination = forms.DateField(
        required=False,
        label='Ordination :',
        label_suffix='',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
            }
        ),
    )

    class Meta:
        model = Monk
        fields = [
            'name',
            'birth',
            'entry',
            'habit',
            'temporary_profession',
            'perpetual_profession',
            'ordination',
        ]
