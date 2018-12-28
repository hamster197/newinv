from django import forms
from django.contrib.auth.models import User

from voronka.models import zayavka_vr


class ChangeRieltForm1(forms.Form):
    a_choises = [(c.id, c.last_name + ' ' + c.first_name) for c in
                 User.objects.filter(is_active=True).order_by('last_name')]
    rielt = forms.ChoiceField(choices=a_choises, label='Выберите месяц:',)