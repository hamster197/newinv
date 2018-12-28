#from datetime# import timezone, datetime
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from voronka.forms import ChangeRieltForm1
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
    coment = post.kom_id.all()
    names_to_exclude = []
    for i in status_klienta_all.objects.filter(zayavka_vr_id_id=post.pk):
        names_to_exclude.append(i.status.status_nazv)
    status_zayav_vibor = status_klienta.objects.all().order_by('status_id').exclude(status_nazv__in=names_to_exclude)
    tek_status_zayav_vibor = status_klienta.objects.all().order_by('-status_id')[0]
    #ss = post.rielt.groups.get().id
    if request.POST:
        usr_form = ChangeRieltForm1(request.POST)#, instance=post)
        if usr_form.is_valid():
            usrid = usr_form.cleaned_data['rielt']
            post.rielt_id = usrid
            post.save()
    usr_form = ChangeRieltForm1()
    return render(request,'voronka/detail.html',{'tn1':n1, 'tn2':n2, 'tpost':post,
                                                 'tek_status_zayav_vibor':tek_status_zayav_vibor, #'ts':ss,
                                                 'tstatus':status_k, 'tstatus_zayav_vibor':status_zayav_vibor,
                                                 'tsur_form':usr_form,'tcoment':coment,
                                                 })

@login_required
def VoronkaChangeView(request, idd, st_id):
    auth = zayavka_vr.objects.get(pk=idd)
    auth_id = auth.rielt_id
    #gr = auth.rielt.groups.get().id
    gr = auth.rielt.groups.get().name
    post = status_klienta_all.objects.create(zayavka_vr_id_id=idd, date_sozd = datetime.now(),
                                             status_id=st_id, auth_id=auth_id, otdel=gr,)
    post.save()
    otd = get_object_or_404(status_klienta, pk = st_id)
    auth.tek_status = otd.status_nazv
    auth.save()
    return redirect('voronka_ap:voronka_detail', idd = idd)#render(request,'voronka/index.html')