from import_export import resources
from .models import RieltsStat
from import_export.fields import Field


class RieltsStatResource(resources.ModelResource):
    last_name = Field(attribute='rielt__last_name', column_name='Фамилия')
    rielt__first_name = Field(attribute='rielt__first_name', column_name='Имя')
    dog_obj = Field(attribute='dog_obj', column_name='Кол-во обьектов в CRM(договор)')
    not_dog_obj = Field(attribute='not_dog_obj', column_name='Кол-во обьектов в CRM(без договора)')
    open_deal = Field(attribute='open_deal', column_name='Cделки открытые(Руб)')
    open_deal_count = Field(attribute='open_deal_count', column_name='Cделки открытые(Счетчик)')
    closed_deal = Field(attribute='closed_deal', column_name='Cделки закрытые(Руб) ')
    closed_deal_count = Field(attribute='closed_deal_count', column_name='Cделки закрытые(Счетчик)')

    class Meta:
        model = RieltsStat
        exclude = ('pk', 'rielt', 'id', 'dog_obj', 'not_dog_obj', 'open_deal', 'open_deal_count',
                   'closed_deal', 'closed_deal_count',)
        #fields = ('rielt__last_name', 'rielt__first_name',)# 'name', 'price',

