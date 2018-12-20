from django.core.validators import MinValueValidator
from django.db import models

class avitoflats(models.Model):
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    DateBegin = models.DateField(verbose_name='Дата начала размещения объявления:')
    DateEnd = models.DateField(verbose_name='Дата окончания публикации объявления:')
    Street = models.CharField(verbose_name='Улица:', help_text='Например Гагарина',max_length=55, blank=False)
    House_Numb = models.CharField(verbose_name='Номер дома:', help_text='например 36', max_length=55, blank=False,
                                  null=False)
    Description = models.TextField(verbose_name='Oписание объявления:', blank=False)
    Price = models.IntegerField(verbose_name='Цена в рублях:', default=800000, validators=[MinValueValidator(300000)])
    #AdStatus_ch = (('Free','Обычное'),('Premium','Премиум-объявление;'),('VIP','VIP-объявление'),
    #               ('PushUp','Поднятие объявления в поиске'),('Highlight','Выделение объявления')
    #               ,('TurboSale','Турбо-продажа'),('QuickSale','Быстрая продажа'))
    AdStatus_ch = (('Обычное','Обычное'),('Премиум-объявление','Премиум-объявление'),('VIP-объявление','VIP-объявление'),
                   ('Поднятие объявления в поиске','Поднятие объявления в поиске'),('Выделение объявления','Выделение объявления')
                   ,('TurboSale','Турбо-продажа'),('QuickSale','Быстрая продажа'))
    AdStatus = models.CharField(verbose_name='Платная услуга:',max_length=55, choices=AdStatus_ch)
    Rooms = models.IntegerField(verbose_name='Количество комнат в квартире:', validators=[MinValueValidator(1)], null=False)
    Square = models.IntegerField(verbose_name='Общая площадь объекта:', blank=False, validators=[MinValueValidator(10)])
    Floor = models.IntegerField(verbose_name='Этаж:', blank=False, validators=[MinValueValidator(1)])
    Floors = models.IntegerField(verbose_name='Количество этажей в доме:', blank=False, validators=[MinValueValidator(1)])
    HouseType_ch = (('Кирпичный','Кирпичный'),('Панельный','Панельный'),('Блочный','Блочный'),
                    ('Монолитный','Монолитный'),('Деревянный','Деревянный'))
    HouseType = models.CharField(verbose_name='Тип дома:',max_length=35, choices=HouseType_ch, blank=False)
    MarketType_ch = (('Вторичка','Вторичка'),('Новостройка','Новостройка'))
    MarketType = models.CharField(verbose_name='Принадлежность квартиры к рынку:', max_length=35, choices=MarketType_ch)
    def __str__(self):
        return self.Street
    class Meta:
        verbose_name = 'Выгрузка на Авито'
        verbose_name_plural = 'Выгрузка на Авито'

class avito_gallery(models.Model):
    id_gal = models.ForeignKey(avitoflats, related_name='idd_gal', verbose_name='Название', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, verbose_name='Дата создания')
    npict = models.ImageField(verbose_name='Фото объекта', upload_to='image/%Y/%m/%d/avito')
    class Meta:
        verbose_name = 'Выгрузки галерея (Avito)'
        verbose_name_plural = 'Выгрузки галерея (Avito)'
