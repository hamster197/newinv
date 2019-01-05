#from datetime# import timezone, datetime
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from voronka.forms import ChangeRieltForm1, NewCommentForm, NewZadachaForm, StatusEdit
from voronka.models import zayavka_vr, status_klienta, status_klienta_all


@login_required
def VoronkaIndexView(request):
    n1 ='Мои '
    n2 = 'Заявки'
    ##########################################
    ### Start of vhodyashe zayavki
    #########################################
    if request.user.groups.get().name == 'Администрация':
        vh_zayav = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'))
        vh_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка')
                                                ).count()
    if request.user.userprofile1.nach_otd == 'Да' and request.user.groups.get().name != 'Администрация':
        otd = request.user.groups.get().name
        vh_zayav = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'),
                                             otdel = otd)
        vh_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'),
                                                otdel = otd).count()
    if request.user.userprofile1.nach_otd != 'Да' and request.user.groups.get().name != 'Администрация':
        usr = request.user
        vh_zayav = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'),
                                             rielt = usr )
        vh_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'),
                                                rielt = usr ).count()
    ##########################################
    ### Start of zayavki in work
    #########################################
    if request.user.groups.get().name == 'Администрация':
        work_zayav = zayavka_vr.objects.all().exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка'])
        work_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка')
                                                ).count()
    if request.user.userprofile1.nach_otd == 'Да' and request.user.groups.get().name != 'Администрация':
        otd = request.user.groups.get().name
        work_zayav = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'),
                                             otdel = otd)
        work_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'),
                                                otdel = otd).count()
    if request.user.userprofile1.nach_otd != 'Да' and request.user.groups.get().name != 'Администрация':
        usr = request.user
        work_zayav = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'),
                                             rielt = usr )
        work_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка с сайта') | Q(tek_status='Входящая заявка'),
                                                rielt = usr ).count()
    return render(request,'voronka/index.html',{'tvh_zayav':vh_zayav,'tvh_zayav_cn':vh_zayav_cn,
                                                'work_zayav':work_zayav, 'twork_zayav_cn':work_zayav_cn,
                                                'tn1':n1, 'tn2':n2})

@login_required
def VoronkaDetailView(request, idd):
    n1 ='Заявки подробно'
    n2 = 'подробно'

    post = zayavka_vr.objects.get(pk=idd)
    #status_k = post.stat_zayv_spr.all()
    #coment = post.kom_id.all().order_by('date_sozd')
    #zadachi = post.zadacha_id.all().order_by('-zadacha_date')

    #names_to_exclude = []
    #for i in status_klienta_all.objects.filter(zayavka_vr_id_id=post.pk):
    #    names_to_exclude.append(i.status.status_nazv)
    #status_zayav_vibor = status_klienta.objects.all().order_by('status_id').exclude(status_nazv__in=names_to_exclude)
    #tek_status_zayav_vibor = status_klienta.objects.all().order_by('-status_id')[0]

    if 'otv_post' in request.POST:
        usr_form = ChangeRieltForm1(request.POST)
        if usr_form.is_valid():
            usrid = usr_form.cleaned_data['rielt']
            post.rielt_id = usrid
            post.save()
    usr_form = ChangeRieltForm1()

    if 'status_post' in request.POST:
        status_form = StatusEdit(request.POST)
        if status_form.is_valid():
            #idd, st_id
            idd = post.pk
            name = status_form.cleaned_data['status_f']
            status_pk = get_object_or_404(status_klienta, status_nazv=name)
            auth_id = post.rielt_id
            gr = post.rielt.groups.get().name
            post = status_klienta_all.objects.create(zayavka_vr_id_id=idd, date_sozd=datetime.now(),
                                                     status_id=status_pk.pk, auth_id=auth_id, otdel=gr, )
            post.save()
            otd = get_object_or_404(status_klienta, pk=status_pk.pk)
            post.tek_status = otd.status_nazv
            post.save()
            post = zayavka_vr.objects.get(pk=idd)
            #n2 = str(idd)+' '+str(status_pk.pk)


    if 'comment_post' in request.POST:
        com_form = NewCommentForm(request.POST)
        if com_form.is_valid():
            comment = com_form.save(commit=False)
            comment.komm_id_id = idd
            comment.save()
    if 'zadacha_post' in request.POST:
        z_form = NewZadachaForm(request.POST)
        if z_form.is_valid():
            zadacha = z_form.save(commit=False)
            zadacha.zadacha_idd_id = idd
            zadacha.save()

    com_form = NewCommentForm()
    zad_form = NewZadachaForm()
    st_form = StatusEdit(initial={'status_f': status_klienta_all, })
    
    return render(request,'voronka/detail.html',{'tn1':n1, 'tn2':n2, 'tpost':post,
                                                 #'tek_status_zayav_vibor':tek_status_zayav_vibor,
                                                  #'tstatus_zayav_vibor':status_zayav_vibor, #'ss':st,
                                                 'tsur_form':usr_form,'tcom_form':com_form,'tst_form':st_form,
                                                 'tzad_form':zad_form,
                                                 })

#@login_required
#def VoronkaChangeView(request, idd, st_id):
#    auth = zayavka_vr.objects.get(pk=idd)
#    auth_id = auth.rielt_id
#    #gr = auth.rielt.groups.get().id
#    gr = auth.rielt.groups.get().name
#    post = status_klienta_all.objects.create(zayavka_vr_id_id=idd, date_sozd = datetime.now(),
#                                             status_id=st_id, auth_id=auth_id, otdel=gr,)
#    post.save()
#    otd = get_object_or_404(status_klienta, pk = st_id)
#    auth.tek_status = otd.status_nazv
#    auth.save()
#    return redirect('voronka_ap:voronka_detail', idd = idd)#render(request,'voronka/index.html')