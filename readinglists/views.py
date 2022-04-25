from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Document


def add_document(request):
    if request.method == 'POST':
        doc = Document.objects.create(
            name=request.POST.get('name'),
            url=request.POST.get('url'),
            description=request.POST.get('description'),
            user=request.user
        )
        new_tags = request.POST.get('tags').split()
        doc.tags.add(*new_tags)
        return redirect(reverse('add-document'))

    return render(request, 'readinglists/add.html', {})


def list_documents(request):
    tag = request.GET.get('tag')
    if tag:
        queryset = Document.objects.filter(tags__name=tag)
    else:
        queryset = Document.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 10)
    try:
        docuements = paginator.page(page)
    except PageNotAnInteger:
        docuements = paginator.page(1)
    except EmptyPage:
        docuements = paginator.page(paginator.num_pages)

    return render(request, 'readinglists/list.html', {'documents': docuements})
