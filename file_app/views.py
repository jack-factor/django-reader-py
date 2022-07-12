from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.contrib import messages
from .forms import DocumentForm
from PyPDF2 import PdfReader
from .models import History


def home(request):
    data = {}
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = handle_uploaded_file(request)
    else:
        form = DocumentForm()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'file_app/home.html', context)


class HistoryListView(LoginRequiredMixin, ListView):
    template_name = 'file_app/history_list.html'
    context_object_name = 'history_list'
    paginate_by = 2

    def get_queryset(self):
        return History.objects.filter(
            user=self.request.user).order_by('-created_at')


class HistoryCreateView(LoginRequiredMixin, CreateView):
    model = History
    fields = ['title', 'file']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def handle_uploaded_file(request):
    f = request.FILES["document"]
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
        messages.success(request, 'Success.')
        return {"file": f, "meta": meta,
                "pages": number_of_pages, "text": text}
    except Exception as e:
        messages.warning(request, 'Invalid file.')
        print(e)
        return result
