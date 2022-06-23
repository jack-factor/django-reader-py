from django.shortcuts import render
from .forms import DocumentForm
from PyPDF2 import PdfReader


def home(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            filename = form.cleaned_data['filename']
            handle_uploaded_file(request.FILES["document"])
            print(filename)
    else:
        form = DocumentForm()

    context = {
        'form': form
    }
    return render(request, 'file_app/home.html', context)


def convet(request):
    context = {}
    return render(request, 'file_app/convert.html', context)


def handle_uploaded_file(f):
    with open('media/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
