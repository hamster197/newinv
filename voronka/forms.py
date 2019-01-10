
from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.forms import extras, DateInput
from material import Row, Layout
from datetime import datetime, timedelta
from voronka.models import comment, zadachi, status_klienta, zayavka_vr


class NewVhZayavForm(forms.ModelForm):
    class Meta:
        model = zayavka_vr
        fields = ['tel','kanal',]

class EditVhZayavForm(forms.ModelForm):
    class Meta:
        model = zayavka_vr
        fields = ['fio','tel','tel_dop','email','kanal','estate','budget',]


class NewWorkZayavForm(forms.ModelForm):
    class Meta:
        model = zayavka_vr
        fields = ['fio','tel','tel_dop','email','kanal','estate','budget',]

class ChangeRieltForm1(forms.Form):
    a_choises = [(c.id, c.last_name + ' ' + c.first_name) for c in
                 User.objects.filter(is_active=True).exclude(username='sait').order_by('last_name')]
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
                                       queryset=status_klienta.objects.exclude(status_nazv__in=['Лид получен','Входящая заявка с сайта','Входящая заявка']).order_by('status_id'))


class OtdSearchForm(forms.Form):
    a_choises = [(c.id, c.name) for c in
                 Group.objects.all().exclude(name__in=['Администрация','Администрация Адлер','Офис-менеджер','Юристы','seo']).order_by('name')]
    otdel = forms.ChoiceField(choices=a_choises, label='Выберите отдел:', )

class RieltSearchForm(forms.Form):
    a_choises = [(c.id, c.last_name + ' ' + c.first_name) for c in
                 User.objects.filter(is_active=True).exclude(username='sait').order_by('last_name')]
    rielt = forms.ChoiceField(choices=a_choises, label='Выберите нового ответсвенного:', )

class MainVoronkaForm(forms.Form):
    stdate = forms.DateField(label='Начало периода',widget=DateInput(attrs={'type': 'date'}),
                             initial=datetime.now() - timedelta(days=datetime.now().day - 1))
    enddate =  forms.DateField(label='Начало периода',widget=DateInput(attrs={'type': 'date'}),
                             initial=datetime.now())
    #def clean(self):
    #    cleaned_data = super(MainVoronkaForm, self).clean()
    #    if datetime(cleaned_data['stdate '])>datetime(cleaned_data['enddate']):
    #            raise ValidationError('Этаж или Этажность равны 0!' , code='invalid')
    #    return cleaned_data