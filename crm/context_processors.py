from datetime import timedelta

from django.db.models import Q

from crm.models import zayavka, flat_obj, otchet_nov
from django.utils import timezone


def main(request):
    n3 = zayavka.objects.filter(status='Свободен').count()
    ds = fdate = str(timezone.datetime.now().year) + '-' + str(timezone.datetime.now().month) + '-' + '01'
    de = str(timezone.datetime.now().year) + '-' + str(timezone.datetime.now().month) + '-' + str(
        timezone.datetime.now().day)
    if not request.user.is_authenticated:
        return {'Ntn3': n3}
    else:
        open_otchet_сn = otchet_nov.objects.filter(
            Q(reelt1=request.user) | Q(reelt2=request.user) | Q(reelt3=request.user)
            | Q(reelt4=request.user) | Q(reelt5=request.user) | Q(
                reelt6=request.user) | Q(reelt7=request.user)
            | Q(reelt8=request.user) | Q(reelt9=request.user) | Q(
                reelt10=request.user),
            date_zakr__gte=ds, sdelka_zakrita='Нет').count()
        closet_otchet_cn = otchet_nov.objects.filter(
            Q(reelt1=request.user) | Q(reelt2=request.user) | Q(reelt3=request.user)
            | Q(reelt4=request.user) | Q(reelt5=request.user) | Q(reelt6=request.user) | Q(reelt7=request.user)
            | Q(reelt8=request.user) | Q(reelt9=request.user) | Q(reelt10=request.user),
            date_zakr__gte=ds, date_zakr__lte=de, sdelka_zakrita='Да').count()
        sriv_otchet_cn = otchet_nov.objects.filter(
            Q(reelt1=request.user) | Q(reelt2=request.user) | Q(reelt3=request.user)
            | Q(reelt4=request.user) | Q(reelt5=request.user) | Q(
                reelt6=request.user) | Q(reelt7=request.user)
            | Q(reelt8=request.user) | Q(reelt9=request.user) | Q(
                reelt10=request.user),
            sdelka_zakrita='Срыв', date_zakr__gte=ds, date_zakr__lte=de).count()
        rasr_otchet_cn = otchet_nov.objects.filter(
            Q(reelt1=request.user) | Q(reelt2=request.user) | Q(reelt3=request.user)
            | Q(reelt4=request.user) | Q(reelt5=request.user) | Q(
                reelt6=request.user) | Q(reelt7=request.user)
            | Q(reelt8=request.user) | Q(reelt9=request.user) | Q(
                reelt10=request.user),
            sdelka_zakrita='Рассрочка').count()
        vestum_count = str(request.user.userprofile1.vestum_count_ads)
        my_ya_obj = flat_obj.objects.filter(author=request.user).count()
        d11 =timezone.datetime.now().date()-timedelta(days=timezone.datetime.now().weekday())
        crm_obj_week_count = flat_obj.objects.filter(author_id=request.user.id, date_sozd__gte=d11).count()
        return {'Ntcrm_obj_week_count':crm_obj_week_count,'Ntn3':n3,'Nt_my_ya_obj':my_ya_obj,
                'topen_otchet_сn':open_otchet_сn, 'tcloset_otchet_cn':closet_otchet_cn,
                'sriv_otchet_cn':sriv_otchet_cn,'trasr_otchet_cn':rasr_otchet_cn,
                'tvestum_count':vestum_count,}
