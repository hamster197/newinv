from django import forms
from django.core.exceptions import ValidationError

from avito.models import avitoflats, avito_gallery


class AvitoEditForm(forms.ModelForm):
    class Meta:
        model = avitoflats
        fields = ('AdStatus','Street','House_Numb','MarketType','HouseType','Floors','Floor','Rooms','Square',
                  'Price','Description')
    def clean(self):
        cleaned_data = super(AvitoEditForm, self).clean()
        if int(cleaned_data['Floors'])<int(cleaned_data['Floor']):
                raise ValidationError('Этаж больше этажности' , code='invalid')
        return cleaned_data

class AvitoGaleryForm(forms.ModelForm):
    class Meta:
        fields = ('npict',)
        model = avito_gallery