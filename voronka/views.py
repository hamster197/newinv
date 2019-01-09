#from datetime# import timezone, datetime
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db.models import Q, Sum
from django.shortcuts import render, get_object_or_404, redirect

from voronka.forms import ChangeRieltForm1, NewCommentForm, NewZadachaForm, StatusEdit, NewVhZayavForm, \
    NewWorkZayavForm, EditVhZayavForm, RieltSearchForm, OtdSearchForm, MainVoronkaForm
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
        vh_zayav = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка',
                                             rielt = usr) | Q(tek_status='Входящая заявка с сайта') )
        vh_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Входящая заявка',
                                             rielt = usr) | Q(tek_status='Входящая заявка с сайта')).count()



    ##########################################
    ### Start of zayavki in work
    #########################################
    if request.user.groups.get().name == 'Администрация':
        work_zayav = zayavka_vr.objects.all().exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Показ/Встреча','Недозвон','Закрыта', 'Закрыта(срыв)'])
        work_zayav_cn = zayavka_vr.objects.all().exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Показ/Встреча','Недозвон','Закрыта', 'Закрыта(срыв)']).count()
    if request.user.userprofile1.nach_otd == 'Да' and request.user.groups.get().name != 'Администрация':
        otd = request.user.groups.get().name
        work_zayav = zayavka_vr.objects.filter(otdel = otd).exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Показ/Встреча','Недозвон','Закрыта', 'Закрыта(срыв)'])
        work_zayav_cn = zayavka_vr.objects.filter(otdel = otd).exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Показ/Встреча','Недозвон','Закрыта', 'Закрыта(срыв)']).count()
    if request.user.userprofile1.nach_otd != 'Да' and request.user.groups.get().name != 'Администрация':
        usr = request.user
        work_zayav = zayavka_vr.objects.filter(rielt = usr).exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Показ/Встреча','Недозвон','Закрыта', 'Закрыта(срыв)'])
        work_zayav_cn = zayavka_vr.objects.filter(rielt = usr).exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Показ/Встреча','Недозвон','Закрыта', 'Закрыта(срыв)']).count()


    ##########################################
    ### Start of pokaz/vstrecha  zayavki
    #########################################
    if request.user.groups.get().name == 'Администрация':
        pokaz_zayav = zayavka_vr.objects.filter(tek_status='Показ/Встреча')
        pokaz_zayav_cn = zayavka_vr.objects.filter(tek_status='Показ/Встреча').count()

    if request.user.userprofile1.nach_otd == 'Да' and request.user.groups.get().name != 'Администрация':
        otd = request.user.groups.get().name
        pokaz_zayav = zayavka_vr.objects.filter(tek_status='Показ/Встреча', otdel = otd)
        pokaz_zayav_cn = zayavka_vr.objects.filter(tek_status='Показ/Встреча', otdel = otd).count()

    if request.user.userprofile1.nach_otd != 'Да' and request.user.groups.get().name != 'Администрация':
        usr = request.user
        pokaz_zayav = zayavka_vr.objects.filter(tek_status='Показ/Встреча', rielt = usr)
        pokaz_zayav_cn = zayavka_vr.objects.filter(tek_status='Показ/Встреча', rielt = usr).count()

    ##########################################
    ### Start of nedozvon  zayavki
    #########################################
    if request.user.groups.get().name == 'Администрация':
        nd_zayav = zayavka_vr.objects.filter(tek_status='Недозвон')
        nd_zayav_cn = zayavka_vr.objects.filter(tek_status='Недозвон').count()

    if request.user.userprofile1.nach_otd == 'Да' and request.user.groups.get().name != 'Администрация':
        otd = request.user.groups.get().name
        nd_zayav = zayavka_vr.objects.filter(tek_status='Недозвон', otdel = otd)
        nd_zayav_cn = zayavka_vr.objects.filter(tek_status='Недозвон', otdel = otd).count()

    if request.user.userprofile1.nach_otd != 'Да' and request.user.groups.get().name != 'Администрация':
        usr = request.user
        nd_zayav = zayavka_vr.objects.filter(tek_status='Недозвон', rielt = usr)
        nd_zayav_cn = zayavka_vr.objects.filter(tek_status='Недозвон', rielt = usr).count()

    ##########################################
    ### Start of zakritie  zayavki
    #########################################
    if request.user.groups.get().name == 'Администрация':
        zakr_zayav = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'))
        zakr_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)')).count()

    if request.user.userprofile1.nach_otd == 'Да' and request.user.groups.get().name != 'Администрация':
        otd = request.user.groups.get().name
        zakr_zayav = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'), otdel = otd)
        zakr_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'), otdel = otd).count()

    if request.user.userprofile1.nach_otd != 'Да' and request.user.groups.get().name != 'Администрация':
        usr = request.user
        zakr_zayav = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'), rielt = usr)
        zakr_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'), rielt = usr).count()


    otssearch = OtdSearchForm()
    if 'otd_search' in request.POST:
        otdform = OtdSearchForm(request.POST)
        if otdform.is_valid():
            name = otdform.cleaned_data['otdel']
            otd = get_object_or_404(Group, id=name)
            vh_zayav = zayavka_vr.objects.filter(tek_status='Входящая заявка',  otdel = name)
            vh_zayav_cn = zayavka_vr.objects.filter(tek_status='Входящая заявка', otdel = name,
                ).count()
            work_zayav = zayavka_vr.objects.filter(otdel=otd).exclude(
                tek_status__in=['Входящая заявка с сайта', 'Входящая заявка',
                                'Показ/Встреча', 'Недозвон', 'Закрыта'])
            work_zayav_cn = zayavka_vr.objects.filter(otdel=otd).exclude(
                tek_status__in=['Входящая заявка с сайта', 'Входящая заявка',
                                'Показ/Встреча', 'Недозвон', 'Закрыта']).count()
            pokaz_zayav = zayavka_vr.objects.filter(tek_status='Показ/Встреча', otdel=otd)
            pokaz_zayav_cn = zayavka_vr.objects.filter(tek_status='Показ/Встреча', otdel=otd).count()
            nd_zayav = zayavka_vr.objects.filter(tek_status='Недозвон', otdel=otd)
            nd_zayav_cn = zayavka_vr.objects.filter(tek_status='Недозвон', otdel=otd).count()
            zakr_zayav = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'), otdel=otd)
            zakr_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'),
                                                      otdel=otd).count()

            gr = get_object_or_404(Group, name=otd)
            n2 = name
            otssearch= OtdSearchForm(initial={'otdel':gr.id})

    rieltsearch = RieltSearchForm()
    if 'rielt_search' in request.POST:
        form = RieltSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['rielt']
            vh_zayav = zayavka_vr.objects.filter(tek_status='Входящая заявка',
                                                   rielt=name)
            vh_zayav_cn = zayavka_vr.objects.filter(tek_status='Входящая заявка',
                                                      rielt=name).count()
            work_zayav = zayavka_vr.objects.filter(rielt=name).exclude(
                tek_status__in=['Входящая заявка с сайта', 'Входящая заявка',
                                'Показ/Встреча', 'Недозвон', 'Закрыта'])
            work_zayav_cn = zayavka_vr.objects.filter(rielt=name).exclude(
                tek_status__in=['Входящая заявка с сайта', 'Входящая заявка',
                                'Показ/Встреча', 'Недозвон', 'Закрыта']).count()
            pokaz_zayav = zayavka_vr.objects.filter(tek_status='Показ/Встреча', rielt=name)
            pokaz_zayav_cn = zayavka_vr.objects.filter(tek_status='Показ/Встреча', rielt=name).count()
            nd_zayav = zayavka_vr.objects.filter(tek_status='Недозвон', rielt=name)
            nd_zayav_cn = zayavka_vr.objects.filter(tek_status='Недозвон', rielt=name).count()
            zakr_zayav = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'), rielt=name)
            zakr_zayav_cn = zayavka_vr.objects.filter(Q(tek_status='Закрыта') | Q(tek_status='Закрыта(срыв)'),
                                                      rielt=name).count()

            rieltsearch = RieltSearchForm(initial={'rielt':name})

    ##########################################
    ### Start of zayavki in task list
    #########################################
    if request.user.groups.get().name == 'Администрация':
        task_zayav = zayavka_vr.objects.all().exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Закрыта', 'Закрыта(срыв)'])
        task_zayav_cn = zayavka_vr.objects.all().exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Закрыта', 'Закрыта(срыв)']).count()
    if request.user.userprofile1.nach_otd == 'Да' and request.user.groups.get().name != 'Администрация':
        otd = request.user.groups.get().name
        task_zayav = zayavka_vr.objects.filter(otdel = otd).exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Закрыта', 'Закрыта(срыв)'])
        task_zayav_cn = zayavka_vr.objects.filter(otdel = otd).exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Закрыта', 'Закрыта(срыв)']).count()
    if request.user.userprofile1.nach_otd != 'Да' and request.user.groups.get().name != 'Администрация':
        usr = request.user
        task_zayav = zayavka_vr.objects.filter(rielt = usr).exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Закрыта', 'Закрыта(срыв)'])
        task_zayav_cn = zayavka_vr.objects.filter(rielt = usr).exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                                      'Закрыта', 'Закрыта(срыв)']).count()
    date = datetime.now()
    zavtra_date = datetime.now()+timedelta(days=1)
    return render(request,'voronka/index.html',{'tvh_zayav':vh_zayav,'tvh_zayav_cn':vh_zayav_cn,
                                                'tdate':date,'tzavtra_date':zavtra_date,
                                                'twork_zayav': work_zayav, 'twork_zayav_cn': work_zayav_cn,
                                                'tpokaz_zayav': pokaz_zayav, 'tpokaz_zayav_cn': pokaz_zayav_cn,
                                                'tnd_zayav': nd_zayav, 'tnd_zayav_cn': nd_zayav_cn,
                                                'tzakr_zayav':zakr_zayav, 'tzakr_zayav_cn':zakr_zayav_cn,
                                                'totssearch':otssearch,'trieltsearch':rieltsearch,
                                                'ttask_zayav':task_zayav,'ttask_zayav_cn':task_zayav_cn,
                                                'tn1':n1, 'tn2':n2})

@login_required
def VoronkaDetailView(request, idd):
    n1 ='Заявки подробно'
    n2 = 'подробно'

    post = zayavka_vr.objects.get(pk=idd)

    if 'otv_post' in request.POST:
        usr_form = ChangeRieltForm1(request.POST)
        if usr_form.is_valid():
            usrid = usr_form.cleaned_data['rielt']
            post.rielt_id = usrid
            post.otdel = post.rielt.groups.get().name
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
            n2= status_pk.pk
            otd = get_object_or_404(status_klienta, pk=status_pk.pk)
            postkl = status_klienta_all.objects.create(zayavka_vr_id_id=idd, date_sozd=datetime.now(),
                                                     status_id=status_pk.pk, auth_id=auth_id, otdel=gr)
            postkl.save()
            otd = get_object_or_404(status_klienta, pk=status_pk.pk)
            post.tek_status = otd.status_nazv
            post.tek_status_date = datetime.now()
            if name == 'Закрыта' or 'Закрыта(срыв)':
                post.date_zakr = datetime.now()
            post.save()
            post = zayavka_vr.objects.get(pk=idd)
            return redirect('voronka_ap:voronka_index')


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
@login_required
def NewZayavVhView(request):
    n1 = 'Новая '
    n2 = 'входящая заявка'
    if request.POST:
        zform = NewVhZayavForm(request.POST)
        if zform.is_valid():
            zayavka = zform.save(commit=False)
            zayavka.date_sozd = datetime.now()
            zayavka.rielt_id = request.user.id
            zayavka.otdel = request.user.groups.get().name
            zayavka.tek_status = 'Входящая заявка'
            zayavka.tek_status_date = datetime.now()
            zayavka.save()
            idz = zayavka.pk
            auth = zayavka_vr.objects.get(pk=idz)
            auth_id = auth.rielt_id
            gr = auth.rielt.groups.get().name
            post = status_klienta_all.objects.create(zayavka_vr_id_id=idz, date_sozd = datetime.now(),
                                                         status_id=1, auth_id=auth_id, otdel=gr,)
            post.save()
            otd = get_object_or_404(status_klienta, pk = 1)
            auth.tek_status = otd.status_nazv
            auth.save()
            return redirect('voronka_ap:voronka_index')
    zform = NewVhZayavForm()
    return render(request,'voronka/newzayav.html',{'tn1':n1,'tn2':n2,'tform':zform})

@login_required
def EditZayavVhView(request, idd):
    n1 = 'Ввод данных '
    n2 = 'входящая заявка'
    if request.POST:
        eform = EditVhZayavForm(request.POST)
        if eform.is_valid():
            zayavka = eform.save(commit=False)
            zayavka.date_vzatia = datetime.now()
            zayavka.rielt_id = request.user.id
            zayavka.otdel = request.user.groups.get().name
            zayavka.tek_status = 'Входящая заявка'
            zayavka.tek_status_date = datetime.now()
            zayavka.save()
            idz = zayavka.pk
            auth = zayavka_vr.objects.get(pk=idz)
            auth_id = auth.rielt_id
            gr = auth.rielt.groups.get().name
            post = status_klienta_all.objects.create(zayavka_vr_id_id=idz, date_sozd = datetime.now(),
                                                         status_id=2, auth_id=auth_id, otdel=gr,)
            post.save()
            otd = get_object_or_404(status_klienta, pk = 2)
            auth.tek_status = otd.status_nazv
            auth.save()
            return redirect('voronka_ap:voronka_index')
    epost = get_object_or_404(zayavka_vr, pk =idd)
    eform = EditVhZayavForm(instance=epost)
    return render(request, 'voronka/newzayav.html', {'tn1': n1, 'tn2': n2, 'tform': eform})


@login_required
def NewZayavWorkView(request):
    n1 = 'Новая '
    n2 = 'заявка(в работе)'
    if request.POST:
        zform = NewWorkZayavForm(request.POST)
        if zform.is_valid():
            zayavka = zform.save(commit=False)
            zayavka.date_sozd = datetime.now()
            zayavka.date_vzatia = datetime.now()
            zayavka.rielt_id = request.user.id
            zayavka.otdel = request.user.groups.get().name
            zayavka.tek_status = 'Входящая заявка'
            zayavka.tek_status_date = datetime.now()
            zayavka.save()
            idz = zayavka.pk
            auth = zayavka_vr.objects.get(pk=idz)
            auth_id = auth.rielt_id
            gr = auth.rielt.groups.get().name
            post = status_klienta_all.objects.create(zayavka_vr_id_id=idz, date_sozd = datetime.now(),
                                                         status_id=2, auth_id=auth_id, otdel=gr,)
            post.save()
            otd = get_object_or_404(status_klienta, pk = 2)
            auth.tek_status = otd.status_nazv
            auth.save()
            return redirect('voronka_ap:voronka_index')

    zform = NewWorkZayavForm()
    return render(request,'voronka/newzayav.html',{'tn1':n1,'tn2':n2,'tform':zform})

@login_required
def VzZayvSaitView(request, idd):
    vpost = get_object_or_404(zayavka_vr, pk = idd)
    idz = vpost.pk
    vpost.rielt = request.user
    vpost.date_vzatia = datetime.now()
    vpost.tek_status = 'Входящая заявка'
    vpost.tek_status_date = datetime.now()
    vpost.save()
    auth = zayavka_vr.objects.get(pk=idz)
    auth_id = auth.rielt_id
    gr = auth.rielt.groups.get().name
    post = status_klienta_all.objects.create(zayavka_vr_id_id=idz, date_sozd=datetime.now(),
                                             status_id=1, auth_id=auth_id, otdel=gr, )
    post.save()
    otd = get_object_or_404(status_klienta, pk=1)
    auth.tek_status = otd.status_nazv
    auth.save()
    return redirect('voronka_ap:voronka_index')


@login_required
def NedozvZayvSaitView(request, idd):
    vpost = get_object_or_404(zayavka_vr, pk = idd)
    idz = vpost.pk
    vpost.rielt = request.user
    vpost.date_vzatia = datetime.now()
    vpost.tek_status = 'Недозвон'
    vpost.tek_status_date = datetime.now()
    vpost.save()
    auth = zayavka_vr.objects.get(pk=idz)
    auth_id = auth.rielt_id
    gr = auth.rielt.groups.get().name
    post = status_klienta_all.objects.create(zayavka_vr_id_id=idz, date_sozd=datetime.now(),
                                             status_id=3, auth_id=auth_id, otdel=gr, )
    post.save()
    otd = get_object_or_404(status_klienta, pk=3)
    auth.tek_status = otd.status_nazv
    auth.save()
    return redirect('voronka_ap:voronka_index')

@login_required
def MainAdmVoronkaView(request):
    n1 = 'Воронка продаж'
    n2 = 'компании'
    start_date = datetime.now() - timedelta(days=datetime.now().day - 1)
    end_date = datetime.now()
    dateform = MainVoronkaForm()
    if request.user.groups.get().name == 'Администрация':
        ############################
        ## Start for obshaya summa 1 tabl
        ############################
        all_zayav_count = zayavka_vr.objects.filter(date_sozd__gte=start_date, date_sozd__lte=end_date).count()
        all_zayav_sum = zayavka_vr.objects.filter(date_sozd__gte=start_date,
                                                    date_sozd__lte=end_date).aggregate(Sum("budget"))
        if all_zayav_sum.get('budget__sum'):
            all_zayav_sum = int(all_zayav_sum.get('budget__sum'))
        else:
            all_zayav_sum = '0'
        #######################################
        work_zayav_count = zayavka_vr.objects.all().exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                                        'Закрыта', 'Закрыта(срыв)']).count()
        work_zayav_sum = zayavka_vr.objects.all().exclude(tek_status__in=['Входящая заявка с сайта','Входящая заявка',
                                         'Закрыта', 'Закрыта(срыв)']).aggregate(Sum("budget"))
        if work_zayav_sum.get('budget__sum'):
            work_zayav_sum =int(work_zayav_sum.get('budget__sum'))
        else:
            work_zayav_sum = '0'
        #######################################
        sdelka_zayav_count = zayavka_vr.objects.filter(tek_status__in=['Закрыта'], #'Закрыта(срыв)'],
                                                       date_sozd__gte=start_date, date_sozd__lte=end_date).count()
        sdelka_zayav_sum = zayavka_vr.objects.filter(tek_status__in=['Закрыта'], #'Закрыта(срыв)'],
                                            date_sozd__gte=start_date, date_sozd__lte=end_date).aggregate(Sum("budget"))
        if sdelka_zayav_sum.get('budget__sum'):
            sdelka_zayav_sum = int(sdelka_zayav_sum.get('budget__sum'))
        else:
            sdelka_zayav_sum = '0'
        return render(request,'voronka/mainvoronka.html',{'tn1':n1,'tn2':n2,'sdate':start_date,'edate':end_date,'tdateform':dateform,
                                                    'tall_zayav_count':all_zayav_count, 'tall_zayav_sum':all_zayav_sum,
                                                    'twork_zayav_count':work_zayav_count, 'twork_zayav_sum':work_zayav_sum,
                                                    'tsdelka_zayav_count':sdelka_zayav_count,'tsdelka_zayav_sum':sdelka_zayav_sum })