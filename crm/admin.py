from django.contrib import admin

from voronka.models import zayavka_vr, status_klienta, status_klienta_all, kanal_pr1, comment, zayavka_subj, zadachi,\
    zadachi_spr
from .models import news, UserProfile1, flat_obj, flat_obj_gal, clients, uchastok, otchet_nov, feed, feed_gallery, \
    zayavka, stat_obj_crm, reyting_po_sdelkam, reyt_sdelka_otd, cachestvoDomCl, domclickText, TmpCianCount, \
    vestum_poryadok_feed
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
#from zvonki.models import zvonok
from avito.models import avitoflats, avito_gallery


class flatgaladm(admin.StackedInline):
    model = flat_obj_gal

class flatfields(admin.ModelAdmin):
    inlines = [flatgaladm]
    list_display = ('pk','author','type','date_sozd','cena_agenstv','adress','dom_numb','kvart_numb',
                    'domclick',)
    list_filter = ['type','domclick','komnat','author']
    search_fields = ['pk']
    fields = ['type','raion','cena_agenstv','adress','dom_numb','kvart_numb','etag',
              'etagnost','author','client_name','client_tel','prim','domclick']
    #ordering = ('adress','dom_numb',)

class flatgalfields(admin.ModelAdmin):
    list_display = ('pk', 'date','id_gal', 'npict')
    list_filter = ['date']

class clientfields(admin.ModelAdmin):
    list_display = ('pk', 'auth','date_sozd','client_fio','budg_do','category','closed')
    list_filter = ['auth','date_sozd','category']
    search_fields = ['pk']

class uchfields(admin.ModelAdmin):
    list_display = ('pk', 'author','client_fio','date_sozd','cena_sobstv','raion','closed')
    search_fields = ['pk', 'autor']
    list_filter = ['date_sozd','author' ]

class sdelka_nov(admin.ModelAdmin):
    list_display = ('date_sozd','date_zakr','nazv_nov', 'fio_kl','rielt','stoimost','komisia','vneseno_komisii','sdelka_zakrita')
    list_filter = ['ot_kuda_kl', 'date_sozd', 'rielt',]

class feedfelds(admin.ModelAdmin):
    list_display = ('pk','date_sozd','nazv','author','prais')
    list_filter = ['date_sozd','pub','author']

class feedgalfelds(admin.ModelAdmin):
    list_display = ('pk','date','id_gal')
    list_filter = ['date',]

class zayavkaFields(admin.ModelAdmin):
    list_display =  ('date_sozd','author','fio','status','reelt_v_rabote','date_vzyatia','kanal')

class statistika_fields(admin.ModelAdmin):
    list_display = ('auth_ful_name','auth_group','crm_calc','cian_calc')

class reytingFields(admin.ModelAdmin):
    list_display = ('auth_ful_name','auth_group','sdelok_calc','sdelok_sum','crm_count','cian_count')

class OtdReytFields(admin.ModelAdmin):
    list_display = ('otd','kommisia')

class KachDMFields(admin.ModelAdmin):
    list_display = ('FIO','otdel','vsego','all_err','text_err','photo_err','kv_numb_err')

class cashDomClickFields(admin.ModelAdmin):
    list_display = ('FIO','otdel','vsego','text_err','photo_err','kv_numb_err','dom_numb_err')

class textFields(admin.ModelAdmin):
    list_display = ('dates','day','text',)
    ordering = ('-day',)

class CianFields(admin.ModelAdmin):
    list_display = ('adler','sochi',)

class ZvonokFields(admin.ModelAdmin):
    list_display = ('pk','tel','subj','raion','cena',)

class VestimPorydok(admin.ModelAdmin):
    list_display = ('date','poryadok',)

class avitogaladm(admin.StackedInline):
    model = avito_gallery

class AvitoFields(admin.ModelAdmin):
    inlines = [avitogaladm]
    list_display = ('auth','DateBegin','DateEnd','AdStatus','Street','House_Numb','Square','Price',)


class stInline(admin.TabularInline):
    #model = zayavka_vr.stat_zayv_spr.through
    model = status_klienta_all#.through

class voronka_fields(admin.ModelAdmin):
    inlines = [stInline]
    list_display = ('pk','rielt','otdel','kanal','tek_status','tek_status_date','budget','date_sozd')

class status_kl_fields(admin.ModelAdmin):
    list_display = ('pk','status_id','status_nazv','voronka_counts',)

class status_kl_all_fields(admin.ModelAdmin):
    list_display = ('date_sozd','status','auth','otdel')

class comment_fields(admin.ModelAdmin):
    list_display = ('date_sozd','comment',)

class zadachi_fields(admin.ModelAdmin):
    list_display = ('zadacha_date','zadacha')

class zadachi_spr_fields(admin.ModelAdmin):
    list_display = ('zadacha',)

class kanal_pr_fields(admin.ModelAdmin):
    list_display = ('pk','kanal','voronka_counts')


admin.site.register(flat_obj, flatfields, )
admin.site.register(otchet_nov, sdelka_nov)
admin.site.register(zayavka, zayavkaFields)
admin.site.register(feed, feedfelds)
admin.site.register(feed_gallery, feedgalfelds)
admin.site.register(stat_obj_crm, statistika_fields)
admin.site.register(reyting_po_sdelkam, reytingFields)
admin.site.register(reyt_sdelka_otd, OtdReytFields)
admin.site.register(cachestvoDomCl, cashDomClickFields)
admin.site.register(TmpCianCount, CianFields)
#admin.site.register(zvonok,ZvonokFields)
admin.site.register(avitoflats, AvitoFields)
admin.site.register(zayavka_vr,voronka_fields)
admin.site.register(status_klienta, status_kl_fields)
admin.site.register(status_klienta_all, status_kl_all_fields)
admin.site.register(kanal_pr1, kanal_pr_fields)
admin.site.register(comment, comment_fields)
admin.site.register(zayavka_subj)#, zadachi_spr_fields)
admin.site.register(zadachi, zadachi_fields)
admin.site.register(zadachi_spr, zadachi_spr_fields)

class UserInline(admin.StackedInline):
    model = UserProfile1
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


