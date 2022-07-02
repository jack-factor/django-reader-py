from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"
    success_message = "the acount %(email)s was created successfully"
