from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from voronka.models import zayavka_vr, status_klienta, status_klienta_all


@login_required
def VoronkaIndexView(request):
    n1 ='Мои '
    n2 = 'Заявки'
    post = zayavka_vr.objects.all()
    return render(request,'voronka/index.html',{'tpost':post, 'tn1':n1, 'tn2':n2})

@login_required
def VoronkaDetailView(request, idd):
    n1 ='Заявки подробно'
    n2 = 'подробно'
    post = zayavka_vr.objects.get(pk=idd)
    status_k = post.stat_zayv_spr.all()
    names_to_exclude = []
    for i in status_klienta_all.objects.filter(zayavka_vr_id_id=post.pk):
        names_to_exclude.append(i.status.status_nazv).order('status_id')
    status_zayav_vibor = status_klienta.objects.all().exclude(status_nazv__in=names_to_exclude)
    return render(request,'voronka/detail.html',{'tn1':n1, 'tn2':n2, 'tpost':post, 'ts':names_to_exclude,
                                                 'tstatus':status_k, 'tstatus_zayav_vibor':status_zayav_vibor,
                                                 })

@login_required
def VoronkaChangeView(request, idd, st_id):
    return render(request,'voronka/index.html')