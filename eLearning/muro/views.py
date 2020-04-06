from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from django.utils import timezone

from .forms import *
from .models import *

@login_required
def muro(request):
    if request.user.is_site_admin:
        return redirect(reverse('muroAdmin'))

    elif request.user.is_professor:
        return redirect(reverse('muroAdmin'))

    return redirect(reverse('muroVer'))

@login_required()
def muroVer(request):
    anuncio_list = Anuncio.objects.all().order_by('-stamp_updated')

    path = request.path.split('/')[1]
    redirect_path = path
    path = path.title()

    search = request.GET.get("search")
    if search:
        anuncio_list = anuncio_list.filter(titulo__startswith=search)

    paginator = Paginator(anuncio_list, 3)


    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "Muro",
        "anuncio_list": queryset,
        "path": path,
        "redirect_path": redirect_path,
    }

    return render(request, "feed/muro.html", context)


@login_required()
def anuncio(request, slug=None):
    add_new_comment = AddNewComment(request.POST or None)
    anuncio_id = Anuncio.objects.get(slug=slug)
    comment_list = Comment.objects.filter(comment_fk=anuncio_id)

    path = request.path.split('/')[1]
    redirect_path = path
    path = path.title()

    context = {
        "title": Anuncio.objects.get(slug=slug).titulo,
        "add_new_comment_form": add_new_comment,
        "path": path,
        "comment_list": comment_list,
        "first_comment": Anuncio.objects.get(slug=slug).texto,
        "first_comment_timestamp": Anuncio.objects.get(slug=slug).stamp_created,
        "first_comment_author": Anuncio.objects.get(slug=slug).author,
        "redirect_path": redirect_path,
    }

    if add_new_comment.is_valid():
        instance = add_new_comment.save(commit=False)
        instance.author = request.user
        instance.comment_fk = Anuncio.objects.get(slug=slug)
        anuncio_object = Anuncio.objects.get(slug=slug)
        anuncio_object.comment_count += 1
        anuncio_object.stamp_updated = timezone.now()
        anuncio_object.save()
        instance.save()
        return redirect(reverse(anuncio, kwargs={'slug': slug,}))

    return render(request, "feed/anuncio.html", context)

@user_passes_test(lambda user: user.is_professor or user.is_site_admin)
def muroAdmin(request):
    anuncio_list = Anuncio.objects.all().order_by('-stamp_updated')
    add_new_anuncio = AddNewAnuncio(request.POST or None)

    path = request.path.split('/')[1]
    redirect_path = path
    path = path.title()

    search = request.GET.get("search")
    if search:
        anuncio_list = anuncio_list.filter(titulo__startswith=search)

    paginator = Paginator(anuncio_list, 3)

    if add_new_anuncio.is_valid():
        instance = add_new_anuncio.save()
        instance.author = request.user.username
        slug = slugify(instance.titulo)
        exists = Anuncio.objects.filter(slug=slug).exists()
        max_id = Anuncio.objects.latest('id').id
        max_id += 1
        # If slug exist append slug by id
        if exists:
            slug = "%s-%s" % (slug, max_id)

        instance.slug = slug
        instance.save()
        return redirect(reverse("muro"))

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "Muro",
        "add_new_anuncio_form": add_new_anuncio,
        "anuncio_list": queryset,
        "path": path,
        "redirect_path": redirect_path,
    }

    return render(request, "feed/muroAdmin.html", context)

