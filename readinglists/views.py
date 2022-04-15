from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Document


def add_document(request):
    if request.method == 'POST':
        Document.objects.create(
            name=request.POST.get('name'),
            url=request.POST.get('url'),
            user=request.user
        )
        return redirect(reverse('add-document'))

    return render(request, 'readinglists/add.html', {})