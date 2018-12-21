from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from avito.forms import AvitoEditForm, AvitoGaleryForm
from avito.models import avitoflats, avito_gallery


@login_required
def newAvitoSub(request):
    n1 = 'Новый объект'
    n2 = 'на Avito'
    if request.POST:
        form = AvitoEditForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auth = request.user
            post.DateBegin = datetime.now()
            post.DateEnd = datetime.now() + timedelta(days=7)
            post.save(form)
            return redirect('avito_ap:Avito_new_galery', idd = post.pk)
    else:
        form = AvitoEditForm(initial={'AdStatus':'Free'})
    return render(request,'avito/edit.html',{'tform':form, 'tn1':n1,'tn2':n2})

@login_required
def AvitoGalView(request, idd):
    n1 = 'Редактировать фото'
    n2 = 'Avito'
    sp = get_object_or_404(avitoflats, pk=idd)
    if request.POST:
        form = AvitoGaleryForm(request.POST, request.FILES)
        if form.is_valid():
            avito_gallery=form.save(commit=False)
            avito_gallery.id_gal_id = idd
            avito_gallery.save()
            return redirect('avito_ap:Avito_new_galery', idd=avito_gallery.id_gal_id)
    else:
        form = AvitoGaleryForm()
        sp = get_object_or_404(avitoflats, pk=idd)
    return render(request,'avito/avitogalform.html',{'tpform':form, 'tn1':n1, 'tn2':n2, 'post':sp})

@login_required
def AvitiGalView(request, idd, sidd):
    spsubj = avito_gallery.objects.get(pk=sidd)
    spsubj.delete()
    sp = get_object_or_404(avitoflats, pk=idd)
    return redirect('avito_ap:Avito_new_galery', idd=sp.pk)

@login_required
def AvitoEditSubjView(request, idd):
    n1 = 'Редактировать объект'
    n2 = 'на Avito'
    subj = get_object_or_404(avitoflats, pk=idd)
    if request.POST:
        form = AvitoEditForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.auth = request.user
            post.DateBegin = datetime.now()
            post.DateEnd = datetime.now() + timedelta(days=7)
            post.save(form)
            return redirect('avito_ap:Avito_new_galery', idd = post.pk)
    else:
        #form = AvitoEditForm()
        form = AvitoEditForm(instance=subj)
    return render(request,'avito/edit.html',{'tform':form, 'tn1':n1,'tn2':n2})

@login_required
def AvitoDellView(request, idd):
    spsubj = avitoflats.objects.get(pk=idd)
    spsubj.delete()
    return redirect('avito_ap:Avito_index')

@login_required
def AvitoIndexView(request):
    n1 = 'Мои обьекты'
    n2 = 'на Авито'
    post = avitoflats.objects.filter(auth=request.user).order_by('-DateEnd')
    return render(request,'avito/index.html',{'tpost':post, 'tn1':n1,'tn2':n2})

@login_required
def AvitoDetailView(request, idd):
    n1 = 'Мой обьект'
    n2 = 'на Авито'
    post = get_object_or_404(avitoflats, pk=idd)
    return render(request,'avito/detail.html',{'tpost':post, 'tn1':n1,'tn2':n2})

def avitoFeedView(request):
    post = avitoflats.objects.all()
    gal = avito_gallery.objects.all()
    return render(request,'avito/avito.html',{'tppost': post, 'tpgal':gal}, content_type="text/xml")

