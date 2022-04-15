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
        docuements = Document.objects.filter(tags__name=tag)
    else:
        docuements = Document.objects.all()
    return render(request, 'readinglists/list.html', {'documents': docuements})
