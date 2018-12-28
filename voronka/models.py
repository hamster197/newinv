from django.contrib.auth.models import User
from django.db import models



class status_klienta(models.Model):
    status_id = models.DecimalField(verbose_name='Статус заявки:(№ пп)', max_digits=5, decimal_places=2,null=True)
    status_nazv = models.CharField(verbose_name='Статус заявки:(Название)', max_length=40, default='')
    def __str__(self):
        return self.status_nazv
    class Meta:
        verbose_name = 'Статус сделки(Справочник)'
        verbose_name_plural = 'Статус сделки(Справочник)'

class status_klienta_all(models.Model):
    zayavka_vr_id = models.ForeignKey('zayavka_vr', on_delete=models.CASCADE, null=True,
                                      related_name='idd_st', verbose_name='Статус заявки:')
    date_sozd = models.DateField(verbose_name='Дата:', null=True, blank=True,)
    status = models.ForeignKey('status_klienta', on_delete=models.CASCADE, null=True, verbose_name='Статус заявки:')
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, verbose_name='Автор:')
    otdel = models.CharField(max_length=45, verbose_name='Отдел')
    def __str__(self):
        return self.otdel
    class Meta:
        verbose_name = 'Статус сделки(Даты)'
        verbose_name_plural = 'Статус сделки(Даты)'

class kanal_pr1(models.Model):
    kanal = models.CharField(max_length=45, verbose_name='Канал привлечения:')
    def __str__(self):
        return self.kanal
    class Meta:
        verbose_name = 'Канал привлечения'
        verbose_name_plural = 'Канал привлечения'

class zayavka_vr(models.Model):
    date_sozd = models.DateField(verbose_name='Дата создания(Входящая заявка):', null=True, blank=True, auto_now=True)
    a_choises = [(c.id, c.last_name + ' ' + c.first_name) for c in
                 User.objects.filter(is_active=True).order_by('last_name')]
    rielt = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, verbose_name='Автор:')
    kanal = models.ForeignKey(kanal_pr1,  on_delete=models.CASCADE, null=True, verbose_name='Канал привлечения:')
    otdel = models.CharField(max_length=55, verbose_name='Oтдел', default='')
    tek_status = models.CharField(max_length=55, verbose_name='Текущий статус', null=True)
    budget = models.IntegerField(verbose_name='Бюджет:', default=800000)
    stat_zayv_spr = models.ManyToManyField(status_klienta_all, related_name='status_zayv_spr', blank=True)
    def __str__(self):
        return str(self.rielt)
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'

class comment(models.Model):
    komm_id = models.ForeignKey(zayavka_vr, related_name='kom_id', on_delete=models.CASCADE, null=True,)
    date_sozd = models.DateTimeField(verbose_name='Дата создания:', auto_now=True)
    comment = models.TextField(verbose_name='Комментарий')
    def __str__(self):
        return str(self.date_sozd)
    class Meta:
        verbose_name_plural = 'Комментарий'
        verbose_name = 'Комментарий'