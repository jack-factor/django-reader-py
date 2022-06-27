from django.shortcuts import render
from django.contrib import messages
from .forms import DocumentForm
from PyPDF2 import PdfReader


def home(request):
    data = {}
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = handle_uploaded_file(request.FILES["document"])
            if len(data) == 0:
                messages.warning(request, 'Invalid file.')
    else:
        form = DocumentForm()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'file_app/home.html', context)


def convert(request):
    context = {}
    return render(request, 'file_app/convert.html', context)


def handle_uploaded_file(f):
    # write
    with open('media/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    # read
    result = {}
    try:
        path = f"media/{f.name}"
        reader = PdfReader(path)
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()
        meta = reader.metadata
        return {"file": f, "meta": meta,
                "pages": number_of_pages, "text": text}
    except Exception as e:
        print(e)
        return result
