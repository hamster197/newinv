
from django import forms
from django.contrib.auth.models import User
from material import Row, Layout

from voronka.models import comment, zadachi, status_klienta_all, status_klienta


class ChangeRieltForm1(forms.Form):
    a_choises = [(c.id, c.last_name + ' ' + c.first_name) for c in
                 User.objects.filter(is_active=True).order_by('last_name')]
    rielt = forms.ChoiceField(choices=a_choises, label='Выберите нового ответсвенного:', )

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('comment',)

class NewZadachaForm(forms.ModelForm):
    class Meta:
        model = zadachi
        fields = ('zadacha_date','zadacha_time','zadacha')
        widgets = {'zadacha_date': forms.TextInput(attrs={'type': 'date'}),
                   'zadacha_time': forms.TextInput(attrs={'type': 'time'})}

    layout = Layout(
                    Row('zadacha_date', 'zadacha_time'),
                    'zadacha'
                    )


class StatusEdit(forms.Form):
    status_f = forms.ModelChoiceField(label='Изменить статус :',
                                       queryset=status_klienta.objects.exclude(status_nazv__in=['Лид получен','Входящая заявка']).order_by('status_id'))
