from django import forms
from django.contrib.auth.models import User

from voronka.models import comment, zadachi, status_klienta_all


class ChangeRieltForm1(forms.Form):
    a_choises = [(c.id, c.last_name + ' ' + c.first_name) for c in
                 User.objects.filter(is_active=True).order_by('last_name')]
    rielt = forms.ChoiceField(choices=a_choises, label='Выберите месяц:',)

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('comment',)

class NewZadachaForm(forms.ModelForm):
    class Meta:
        model = zadachi
        fields = ('zadacha_date','zadacha')
        widgets = {'zadacha_date': forms.TextInput(attrs={'type': 'date'})}

class StatusEdit(forms.Form):
    status_f = forms.ChoiceField(  label='Сменить статус :', )#initial=moth_ch,
